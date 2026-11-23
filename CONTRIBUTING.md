# Contributing

## Layout

```
data/
├── projects.json                     # project name -> open-source repo URL
└── <series>/<edition>/               # e.g. kubecon/na-2026
    ├── event.json                    # name, playlists, Sched host, tracks
    ├── videos.jsonl                  # every video in the playlists (ingest)
    ├── talks/<video-id>.json         # one summary per talk (source of truth)
    └── talks.jsonl                   # all talks, one per line (generated)
events/<series>/<edition>/            # generated Markdown, do not edit by hand
schema/talk.schema.json               # talk JSON contract
prompts/extract.md                    # summarization prompt (versioned)
pipeline/                             # ingest, transcript, extract, render
```

Only `data/` and `README.md` outside the summaries block are edited by hand. `events/`, `talks.jsonl` and the README summaries block are rewritten by `render.py`.

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv venv --managed-python --python 3.12 .venv
uv pip install --python .venv/bin/python -r requirements.txt
```

`--managed-python` matters on hosts whose system Python is built against a FIPS TLS library; `yt-dlp` fails there with `No cipher can be selected`.

## Pipeline

| Step | Command | Writes |
|---|---|---|
| 1. List videos | `.venv/bin/python pipeline/ingest.py --event kubecon/na-2026` | `data/kubecon/na-2026/videos.jsonl` |
| 2. Transcripts | `.venv/bin/python pipeline/transcript.py <video_id> ...` | `.cache/` (not committed) |
| 3. Summarize | `AWS_PROFILE=<profile> .venv/bin/python pipeline/extract.py --event kubecon/na-2026 <video_id> ...` | `data/kubecon/na-2026/talks/<id>.json` |
| 4. Render | `.venv/bin/python pipeline/render.py` | `events/`, `talks.jsonl`, README summaries block |

Step 3 calls Claude on Amazon Bedrock. Override the model with `MODEL_ID`, the region with `AWS_REGION`. Every step skips or overwrites per video, so re-running is safe.

Never commit transcripts. Only summaries are published.

## Add an event

1. Create `data/<series>/<edition>/event.json`:

   ```json
   {
     "name": "KubeCon + CloudNativeCon Europe 2027",
     "series": "KubeCon + CloudNativeCon",
     "playlists": ["https://www.youtube.com/playlist?list=<id>"],
     "sched_host": "<edition>.sched.com",
     "tracks": {"main": "Main conference", "unassigned": "Track not yet assigned"},
     "track_of": {}
   }
   ```

2. Run the four pipeline steps with `--event <series>/<edition>`.

`sched_host` is optional. Without it, slides render as `-`.

## Co-located events and tracks

One edition can hold many co-located events. Each talk's summary stays at `events/<series>/<edition>/talks/<id>.md`, so links never move. The track only decides which section a talk is listed under.

1. Add the track to `tracks`, e.g. `"llm-d-day": "llm-d Community Day (co-located)"`.
2. Map talks to it in `track_of`: `"gC7GfYxrZgI": "llm-d-day"`.
3. Run `render.py`.

Talks not in `track_of` appear under **Track not yet assigned**. YouTube does not say which co-located event a talk belongs to, so take the track from the event schedule.

## Slides

Sched blocks scripted access, so `extract.py` writes a Sched search link (`"status": "search"`). To add a direct link, edit the talk JSON:

```json
"slides": {"status": "direct", "url": "https://static.sched.com/..."}
```

## Project links

The **Projects mentioned** list links any name that matches a key in `data/projects.json`. Add only open-source projects, linking to the main repo. Names in talk JSON must match the key exactly.

## Changing the prompt

Bump the version comment in `prompts/extract.md` and `PROMPT_VERSION` in `pipeline/extract.py` together. Each talk JSON records the `prompt_version` it was made with.

## Fixing a summary

Edit `data/<series>/<edition>/talks/<id>.json`, run `render.py`, and open a PR. Every point needs a `t` (seconds into the video) that points to where it is said.
