"""Summarize cached transcripts into data/<series>/<edition>/talks/<id>.json with Claude on Bedrock."""
import argparse
import json
import os
import re
from pathlib import Path

import boto3
import jsonschema

from common import (clean_title, event_dir, load_event, load_meta, load_videos, slides_link,
                    speakers_from_title, youtube_url)

ROOT = Path(__file__).resolve().parent.parent
MODEL_ID = os.environ.get("MODEL_ID", "global.anthropic.claude-sonnet-5-5")
PROMPT_VERSION = "extract-v1"


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--event", required=True, help="<series>/<edition>, e.g. kubecon/na-2026")
    p.add_argument("video_ids", nargs="+")
    a = p.parse_args()

    schema = json.loads((ROOT / "schema" / "talk.schema.json").read_text())
    template = (ROOT / "prompts" / "extract.md").read_text()
    ev = load_event(a.event)
    videos = load_videos(a.event)
    out_dir = event_dir(a.event) / "talks"
    out_dir.mkdir(parents=True, exist_ok=True)
    client = boto3.client("bedrock-runtime", region_name=os.environ.get("AWS_REGION", "us-east-1"))

    for vid in a.video_ids:
        v, m = videos[vid], load_meta(vid)
        title = m["full_title"]
        meta = {
            "video_id": vid,
            "event": a.event,
            "title": clean_title(title),
            "speakers": speakers_from_title(title),
            "duration_s": v["duration_s"],
            "youtube_url": youtube_url(vid),
            "slides": slides_link(ev, title),
        }
        prompt = (template
                  .replace("{{SCHEMA}}", json.dumps(schema))
                  .replace("{{METADATA}}", json.dumps(meta))
                  .replace("{{TRANSCRIPT}}", (ROOT / ".cache" / "transcripts" / f"{vid}.txt").read_text()))
        resp = client.converse(
            modelId=MODEL_ID,
            messages=[{"role": "user", "content": [{"text": prompt}]}],
            inferenceConfig={"maxTokens": 4096},
        )
        text = resp["output"]["message"]["content"][0]["text"]
        talk = json.loads(re.search(r"\{.*\}", text, re.S).group(0))
        talk.update(meta)
        talk["prompt_version"] = PROMPT_VERSION
        jsonschema.validate(talk, schema)
        (out_dir / f"{vid}.json").write_text(json.dumps(talk, indent=2, ensure_ascii=False) + "\n")
        print(f"{vid} ok")


if __name__ == "__main__":
    main()
