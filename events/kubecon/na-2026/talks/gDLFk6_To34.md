# Running Secure Agents at Scale

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Carlos Sanchez (Adobe)  
**Video:** [YouTube](https://www.youtube.com/watch?v=gDLFk6_To34) (29:56)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Running+Secure+Agents+at+Scale)  
**Tags:** `agents`, `agent-sandbox`, `sandboxing`, `browser-automation`, `multi-tenancy`

> Adobe Experience Manager runs a few thousand single-tenant agents that import and redesign customer websites, each needing a sandboxed Playwright browser. After comparing Agent Sandbox, OpenShell, Substrate and others, Adobe chose Agent Sandbox with warm pools because its agents run long sessions rather than short bursts.

## Key points

- Customers chat with an agent that imports a site into the platform and edits its design, with a live preview; Adobe needs to run a few thousand of these agents. [1:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=60s)
- Design: one user per pod, because agents hold state and can write and run code; persistent storage for generated files; no credentials stored in the agent, since agents can be tricked into exfiltrating them. [2:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=120s)
- Pain points: read-write-once volumes cause downtime when a user's pod is replaced, large images (browsers, Playwright) slow cold starts, and idle agents waste resources. [3:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=180s)
- Playwright runs in its own sandbox, separate from the agent: Chromium is stateful and cannot be shared across users, and splitting lifecycles keeps the agent from paying the browser's startup cost when a chat does not need it. [5:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=300s)
- Options compared in a public repo: Agent Sandbox (warm pools, gVisor or Kata), OpenShell (built on Agent Sandbox, adds a supervisor for policy, DNS and credential injection), Substrate (own scheduler, suspend and resume with snapshots), and smaller projects. [9:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=540s)
- A Playwright proxy maps each caller to a browser sandbox by looking up the calling pod's labels from its source IP; labels are trusted because agents have no Kubernetes API access, while request contents could be faked. [13:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=780s)
- Agent Sandbox resources: SandboxTemplate (pod spec), warm pool (replica count per template), SandboxClaim (takes a sandbox from the pool) and Sandbox, all managed by its controller. Deleting the claim gives a fresh browser. [16:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=960s)
- Substrate was not chosen: it was early and has many moving parts, and its suspend/resume fits bursty, mostly idle agents, while Adobe's agents run for hours. [18:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=1080s)
- Selection guide: Agent Sandbox for fast assignment and simplicity, OpenShell for more policy and services around the agent, Substrate for bursty short-lived workloads; the speaker notes cloud providers appear to be converging on Substrate. [22:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=1320s)
- Production setup keeps a warm pool of three Playwright sandboxes; clients needed no code change, only a remote Playwright endpoint. Readiness means waiting until Chromium's ports are open. [24:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=1440s)
- Q&A: agent pods are Claude Code clients that call the LLM and use Playwright as a tool; the sandbox runtime is gVisor, which the speaker sees as the most supported. [28:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=1680s)

## Numbers stated

- A few thousand agents to run. [0:00](https://www.youtube.com/watch?v=gDLFk6_To34)
- Warm pool of three Playwright sandbox replicas kept running. [24:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=1440s)

## Open gaps

- Most volumes can only be mounted for writing by one pod, so replacing a user's pod causes downtime. [4:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=240s)
- Not everything Playwright offers is exposed through MCP yet, so Adobe also exposes WebSockets. [6:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=360s)
- Warm pools cost resources while idle sandboxes wait, and the sandboxing landscape is changing week to week. [15:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=900s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| learn | Study the speaker's public repo that runs Playwright on each sandbox implementation and compares them. | [7:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=420s) |
| build | Put heavy tools like browsers in their own warm-pooled sandboxes behind a proxy that assigns them by pod identity, not by request contents. | [26:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=1560s) |
| write | Benchmark sandbox startup time and resource cost for long-running versus bursty agent workloads across Agent Sandbox, OpenShell and Substrate. | [27:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=1620s) |
| contribute | Give feedback to Agent Sandbox on lifecycle and readiness handling for stateful tools like Chromium. | [26:00](https://www.youtube.com/watch?v=gDLFk6_To34&t=1560s) |

## Projects mentioned

[Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox), OpenShell, Substrate, Playwright, Chromium, [gVisor](https://github.com/gvisor/gvisor), Kata Containers, Claude Code, OpenClaw, [Kubernetes](https://github.com/kubernetes/kubernetes)
