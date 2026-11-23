"""List the playlists in data/<series>/<edition>/event.json into videos.jsonl."""
import argparse
import json
import subprocess
import sys
from pathlib import Path

from common import event_dir, load_event


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--event", required=True, help="<series>/<edition>, e.g. kubecon/na-2026")
    a = p.parse_args()

    seen, rows = set(), []
    for url in load_event(a.event)["playlists"]:
        pl = json.loads(subprocess.run(
            [str(Path(sys.executable).parent / "yt-dlp"), "--flat-playlist", "-J", url],
            check=True, capture_output=True, text=True,
        ).stdout)
        for e in pl["entries"]:
            if e["id"] in seen:
                continue
            seen.add(e["id"])
            rows.append({
                "video_id": e["id"],
                "title": e["title"],
                "duration_s": int(e.get("duration") or 0),
                "playlist_id": pl["id"],
                "playlist_title": pl["title"],
            })

    dest = event_dir(a.event) / "videos.jsonl"
    dest.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    print(f"{len(rows)} videos -> {dest}")


if __name__ == "__main__":
    main()
