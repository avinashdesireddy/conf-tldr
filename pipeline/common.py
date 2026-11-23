import json
import re
from pathlib import Path
from urllib.parse import quote_plus

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def event_dir(event: str) -> Path:
    """event is '<series>/<edition>', e.g. 'kubecon/na-2026'."""
    return DATA / event


def load_event(event: str) -> dict:
    return json.loads((event_dir(event) / "event.json").read_text())


def list_events() -> list[str]:
    return sorted(str(p.parent.relative_to(DATA)) for p in DATA.glob("*/*/event.json"))


def load_projects() -> dict:
    return json.loads((DATA / "projects.json").read_text())


def load_videos(event: str) -> dict:
    rows = [json.loads(l) for l in (event_dir(event) / "videos.jsonl").read_text().splitlines() if l]
    return {r["video_id"]: r for r in rows}


def load_meta(vid: str) -> dict:
    return json.loads((ROOT / ".cache" / "meta" / f"{vid}.json").read_text())


def track_of(ev: dict, vid: str) -> str:
    return ev.get("track_of", {}).get(vid, "unassigned")


def youtube_url(vid: str, t: int | None = None) -> str:
    return f"https://www.youtube.com/watch?v={vid}" + (f"&t={t}s" if t else "")


def clean_title(title: str) -> str:
    return title.rsplit(" - ", 1)[0].rstrip(". ")


def slides_link(ev: dict, title: str) -> dict:
    """Sched blocks scripted fetches (Cloudflare), so slides default to a search link."""
    host = ev.get("sched_host")
    if not host:
        return {"status": "none", "url": None}
    return {"status": "search", "url": f"https://{host}/search?q={quote_plus(clean_title(title))}"}


def speakers_from_title(title: str) -> list[dict]:
    """'A, OrgA & B, OrgB' or 'A, OrgA, B, OrgB & C, OrgC'. Names only when orgs are missing."""
    if " - " not in title:
        return []
    items = [s.strip() for s in re.split(r",|\s&\s", title.rsplit(" - ", 1)[1]) if s.strip()]
    if len(items) % 2:
        return [{"name": n} for n in items]
    return [{"name": items[i], "org": items[i + 1]} for i in range(0, len(items), 2)]
