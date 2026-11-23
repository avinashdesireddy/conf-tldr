"""Validate data/<series>/<edition>/talks/*.json and render Markdown under events/ plus the README summary table."""
import json
import re
from pathlib import Path

import jsonschema

from common import ROOT, event_dir, list_events, load_event, load_projects, load_videos, track_of, youtube_url

START, END = "<!-- summaries:start -->", "<!-- summaries:end -->"


def ts(t: int) -> str:
    return f"{t // 60}:{t % 60:02d}"


def cite(vid: str, t: int) -> str:
    return f"[{ts(t)}]({youtube_url(vid, t)})"


def slides_md(slides: dict, short: bool = False) -> str:
    if slides["status"] == "direct":
        return f"[Slides]({slides['url']})"
    if slides["status"] == "search":
        return f"[{'Sched' if short else 'Find slides on Sched'}]({slides['url']})"
    return "-"


def project_md(name: str, projects: dict) -> str:
    return f"[{name}]({projects[name]})" if name in projects else name


def render_talk(d: dict, ev: dict, projects: dict) -> str:
    vid = d["video_id"]
    speakers = ", ".join(f"{s['name']} ({s['org']})" if s.get("org") else s["name"] for s in d["speakers"])
    out = [
        f"# {d['title']}",
        "",
        f"**Event:** {ev['name']} · {ev['tracks'][track_of(ev, vid)]}  ",
        f"**Speakers:** {speakers}  ",
        f"**Video:** [YouTube]({d['youtube_url']}) ({ts(d.get('duration_s', 0))})  ",
        f"**Slides:** {slides_md(d['slides'])}  ",
        f"**Tags:** {', '.join(f'`{t}`' for t in d.get('tags', []))}",
        "",
        f"> {d['tldr']}",
        "",
        "## Key points",
        "",
        *[f"- {p['text']} {cite(vid, p['t'])}" for p in d["key_points"]],
    ]
    if d.get("numbers"):
        out += ["", "## Numbers stated", "", *[f"- {p['text']} {cite(vid, p['t'])}" for p in d["numbers"]]]
    out += [
        "", "## Open gaps", "", *[f"- {p['text']} {cite(vid, p['t'])}" for p in d["open_gaps"]],
        "", "## Opportunities", "",
        "| Type | Opportunity | At |", "|---|---|---|",
        *[f"| {o['type']} | {o['text']} | {cite(vid, o['t'])} |" for o in d["opportunities"]],
        "", "## Projects mentioned", "", ", ".join(project_md(p, projects) for p in d["projects"]),
        "",
    ]
    return "\n".join(out)


def talk_rows(talks: list[dict], link_prefix: str) -> list[str]:
    rows = ["| Talk | Speakers | Video | Slides |", "|---|---|---|---|"]
    for d in sorted(talks, key=lambda x: x["title"]):
        rows.append(
            f"| [{d['title']}]({link_prefix}talks/{d['video_id']}.md) "
            f"| {', '.join(s['name'] for s in d['speakers'])} "
            f"| [YouTube]({d['youtube_url']}) | {slides_md(d['slides'], short=True)} |"
        )
    return rows


def by_track(ev: dict, talks: list[dict]) -> list[tuple[str, list[dict]]]:
    groups = []
    for key, label in ev["tracks"].items():
        members = [d for d in talks if track_of(ev, d["video_id"]) == key]
        if members:
            groups.append((label, members))
    return groups


def render_event_index(ev: dict, talks: list[dict]) -> str:
    out = [f"# {ev['name']}", "", f"{len(talks)} talks summarized. [Status of all talks](STATUS.md)", ""]
    for label, members in by_track(ev, talks):
        out += [f"## {label}", "", *talk_rows(members, ""), ""]
    return "\n".join(out)


MIN_DURATION_S = 300


def render_status(event: str, ev: dict, talks: list[dict]) -> str:
    """Checklist of every playlist video of 5+ minutes: done (has a summary) or to do."""
    done = {d["video_id"] for d in talks}
    videos = [v for v in load_videos(event).values() if v["video_id"] in done or v["duration_s"] >= MIN_DURATION_S]

    def item(v: dict) -> str:
        vid = v["video_id"]
        if vid in done:
            return f"- [x] {v['title']} · [summary](talks/{vid}.md) · [YouTube]({youtube_url(vid)})"
        return f"- [ ] {v['title']} · [YouTube]({youtube_url(vid)})"

    todo = [item(v) for v in videos if v["video_id"] not in done]
    return "\n".join([
        f"# {ev['name']}: status", "",
        f"## Done ({len(done)})", "", *[item(v) for v in videos if v["video_id"] in done], "",
        f"## To do ({len(todo)})", "", *todo, "",
    ])


def render_readme_block(events: list[tuple[str, dict, list[dict]]]) -> str:
    out = [START, ""]
    for event, ev, talks in events:
        out += [f"### {ev['name']}", "", f"[Status of all talks](events/{event}/STATUS.md)", ""]
        for label, members in by_track(ev, talks):
            out += [f"**{label}**", "", *talk_rows(members, f"events/{event}/"), ""]
    out.append(END)
    return "\n".join(out)


def main() -> None:
    schema = json.loads((ROOT / "schema" / "talk.schema.json").read_text())
    projects = load_projects()
    rendered = []

    for event in list_events():
        ev = load_event(event)
        dest = ROOT / "events" / event
        (dest / "talks").mkdir(parents=True, exist_ok=True)
        talks = []
        for f in sorted((event_dir(event) / "talks").glob("*.json")):
            d = json.loads(f.read_text())
            jsonschema.validate(d, schema)
            (dest / "talks" / f"{d['video_id']}.md").write_text(render_talk(d, ev, projects))
            talks.append(d)
        if not talks:
            continue
        (dest / "README.md").write_text(render_event_index(ev, talks))
        (dest / "STATUS.md").write_text(render_status(event, ev, talks))
        (event_dir(event) / "talks.jsonl").write_text("".join(json.dumps(d, ensure_ascii=False) + "\n" for d in talks))
        rendered.append((event, ev, talks))
        print(f"{event}: {len(talks)} talks")

    readme = ROOT / "README.md"
    text = readme.read_text()
    if START not in text or END not in text:
        raise SystemExit(f"README.md is missing {START} / {END}")
    readme.write_text(re.sub(re.escape(START) + r".*?" + re.escape(END),
                             lambda _: render_readme_block(rendered), text, count=1, flags=re.S))


if __name__ == "__main__":
    main()
