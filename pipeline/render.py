"""Validate data/<series>/<edition>/talks/*.json and render Markdown under events/ plus the README summary table."""
import json
import re
from pathlib import Path

import jsonschema

from common import (ROOT, clean_title, event_dir, list_events, load_event, load_projects, load_videos, track_of,
                    youtube_url)

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
    out = [f"# {ev['name']}", "", f"{len(talks)} talks summarized.", ""]
    for label, members in by_track(ev, talks):
        out += [f"## {label}", "", *talk_rows(members, ""), ""]
    return "\n".join(out)


def short_title(playlist_title: str) -> str:
    """Playlist titles end in ' - Speakers' or '... Speakers' (truncated by YouTube)."""
    if "..." in playlist_title:
        return playlist_title.split("...")[0].rstrip(" .:,") + "…"
    return clean_title(playlist_title)


def render_readme_block(events: list[tuple[str, dict, list[dict]]]) -> str:
    """Per event, the talks listed in topics.json; a title links to its summary once one exists."""
    out = [START, ""]
    for event, ev, talks in events:
        topics_path = event_dir(event) / "topics.json"
        topics = json.loads(topics_path.read_text()) if topics_path.exists() else {}
        summaries = {d["video_id"]: d for d in talks}
        videos = load_videos(event)
        listed = {vid for ids in topics.values() for vid in ids}
        other = [vid for vid in summaries if vid not in listed]
        if other:
            topics = {**topics, "Other": other}

        out += [f"### {ev['name']}", ""]
        for topic, ids in topics.items():
            out += [f"#### {topic}", "", "| Talk | Video |", "|---|---|"]
            for vid in ids:
                if vid in summaries:
                    talk = f"[{summaries[vid]['title']}](events/{event}/talks/{vid}.md)"
                else:
                    talk = short_title(videos[vid]["title"])
                out.append(f"| {talk} | [YouTube]({youtube_url(vid)}) |")
            out.append("")
    out.append(END)
    return "\n".join(out)


RAW = "https://raw.githubusercontent.com/avinashdesireddy/conf-tldr/main"


def render_llms_txt(events: list[tuple[str, dict, list[dict]]]) -> str:
    """llms.txt (llmstxt.org): GitMCP reads this first, so it must list every summary by absolute URL."""
    out = ["# Talk Radar (conf-tldr)", "",
           "> Summaries of conference talks. Each has key points with video timestamps, numbers the speakers "
           "shared, open gaps, opportunities, and links to slides and open-source projects.", "",
           f"Structured data for every talk: {RAW}/data/<series>/<edition>/talks.jsonl", ""]
    for event, ev, talks in events:
        out += [f"## {ev['name']}", ""]
        for d in sorted(talks, key=lambda d: d["title"]):
            out.append(f"- [{d['title']}]({RAW}/events/{event}/talks/{d['video_id']}.md): {d['tldr']}")
        out.append("")
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
        (event_dir(event) / "talks.jsonl").write_text("".join(json.dumps(d, ensure_ascii=False) + "\n" for d in talks))
        rendered.append((event, ev, talks))
        print(f"{event}: {len(talks)} talks")

    (ROOT / "llms.txt").write_text(render_llms_txt(rendered))

    readme = ROOT / "README.md"
    text = readme.read_text()
    if START not in text or END not in text:
        raise SystemExit(f"README.md is missing {START} / {END}")
    readme.write_text(re.sub(re.escape(START) + r".*?" + re.escape(END),
                             lambda _: render_readme_block(rendered), text, count=1, flags=re.S))


if __name__ == "__main__":
    main()
