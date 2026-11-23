"""Fetch English captions into .cache/transcripts/<id>.{json,txt}. Not published."""
import argparse
import json
import subprocess
import sys
from pathlib import Path

from youtube_transcript_api import YouTubeTranscriptApi

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "transcripts"
META = ROOT / ".cache" / "meta"


def fetch_meta(vid: str) -> None:
    """Playlist titles are truncated; the description carries the full title and abstract."""
    if (META / f"{vid}.json").exists():
        return
    d = json.loads(subprocess.run(
        [str(Path(sys.executable).parent / "yt-dlp"), "--skip-download", "-j", f"https://www.youtube.com/watch?v={vid}"],
        check=True, capture_output=True, text=True,
    ).stdout)
    lines = [l.strip() for l in d.get("description", "").splitlines() if l.strip()]
    body = [l for l in lines if "kubecon.io" not in l]
    (META / f"{vid}.json").write_text(json.dumps({
        "video_id": vid,
        "full_title": body[0] if body else d["title"],
        "abstract": " ".join(body[1:]),
        "upload_date": d.get("upload_date"),
    }, ensure_ascii=False))


def to_minute_lines(rows: list[dict]) -> str:
    lines, cur, buf = [], None, []
    for r in rows:
        b = int(r["start"] // 60)
        if b != cur:
            if buf:
                lines.append(f"[{cur * 60}] " + " ".join(buf))
            cur, buf = b, []
        buf.append(r["text"].replace("\n", " "))
    if buf:
        lines.append(f"[{cur * 60}] " + " ".join(buf))
    return "\n".join(lines)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("video_ids", nargs="+")
    a = p.parse_args()

    CACHE.mkdir(parents=True, exist_ok=True)
    META.mkdir(parents=True, exist_ok=True)
    api = YouTubeTranscriptApi()
    for vid in a.video_ids:
        fetch_meta(vid)
        if (CACHE / f"{vid}.txt").exists():
            print(f"{vid} cached")
            continue
        rows = [{"start": round(s.start, 1), "text": s.text} for s in api.fetch(vid, languages=["en"])]
        (CACHE / f"{vid}.json").write_text(json.dumps(rows))
        (CACHE / f"{vid}.txt").write_text(to_minute_lines(rows))
        print(f"{vid} {len(rows)} segments")


if __name__ == "__main__":
    main()
