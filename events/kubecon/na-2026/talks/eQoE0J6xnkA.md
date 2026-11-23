# Demystifying Upgrades for Stateful, Dormant AI Agents: Unleashing Seamless Updates in Dynamic Sand

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Zhang Zhen (Alibaba Group)  
**Video:** [YouTube](https://www.youtube.com/watch?v=eQoE0J6xnkA) (31:16)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Demystifying+Upgrades+for+Stateful%2C+Dormant+AI+Agents%3A+Unleashing+Seamless+Updates+in+Dynamic+Sand)  
**Tags:** `agents`, `sandboxes`, `upgrades`, `stateful-workloads`, `kubernetes-operators`

> Cloud-hosted agent sandboxes need near-daily harness and CVE updates, but their state (sessions, skills, installed tools) sits in the container's writable layer and is lost on restart. OpenKruise Agents offers upgrade paths for warm pools, sandbox claims, and running or paused sandboxes, plus a session-aware sandbox service for fleet-level rollouts.

## Key points

- Agent harnesses need frequent, often daily, updates for features and CVE patches, while sandbox state such as session context, skills and installed tools is lost when the sandbox restarts. [1:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=60s)
- Sandboxes lack Deployment- or StatefulSet-style workload support, so phased rollout and replica control are left to operators. [2:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=120s)
- Lifecycle: ready in a warm pool, running once claimed with a session, then idle and usually paused to save compute. [2:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=120s)
- OpenKruise Agents uses pods as sandboxes and exposes an E2B API for AI engineers and a Kubernetes API for infra teams; storage can be static mounts or on-demand mounts set at claim time. [4:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=240s)
- Warm pool refresh is easy: the sandbox set behaves like a Deployment, with max-unavailable and max-surge controls. [7:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=420s)
- At claim time the image can be swapped (e.g. to a canary) and resources raised through in-place pod resizing, so a small warm pool can serve larger requests. [8:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=480s)
- Idle detection is time-based or probe-based: a node daemon repeatedly runs a command in the sandbox asking the agent whether it has active sessions. [9:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=540s)
- A sandbox update job selects sandboxes by label and state; paused sandboxes are woken, upgraded and paused again. [11:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=660s)
- Core problem: you cannot freely change the image (lower layer) while keeping the overlay writable layer; mixing them gives an unpredictable file system. [12:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=720s)
- Strategies for running sandboxes: recreate with pre/post-upgrade backup hooks, in-place update (e.g. sidecars, or emptyDir as backup), checkpoint-restore for non-image changes, and an installer upgrade that injects an ephemeral container to copy in new files. [14:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=840s)
- Sandbox service gives a stable endpoint; a gateway maps session IDs to sandboxes and drains old sandboxes during a rollout. [21:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=1260s)

## Numbers stated

- In production about 99% of sandboxes are hibernated; only 1 in 100 is running. [3:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=180s)

## Open gaps

- Recreate upgrades require knowing which data to save and having shared storage, and LLMs may install files outside the directory you told them to use. [27:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=1620s)
- Agent applications have poor backward compatibility between versions, so upgrades can break; checkpoint-then-rollback is planned for risky upgrades. [28:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=1680s)
- The installer upgrade strategy is not released yet; it is planned for the next release. [25:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=1500s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Take a file-system-only checkpoint before each agent sandbox upgrade and roll back to it if the upgrade fails. | [28:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=1680s) |
| build | Add an idle probe to your agent harness that reports active sessions, so upgrades only touch idle sandboxes. | [10:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=600s) |
| learn | How the overlay file system splits image layers from the writable layer, and why that blocks naive in-place image upgrades. | [12:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=720s) |
| contribute | Try the sandbox upgrade strategies in OpenKruise Agents and report agent-specific state that hooks fail to capture. | [25:00](https://www.youtube.com/watch?v=eQoE0J6xnkA&t=1500s) |

## Projects mentioned

OpenKruise, [Kubernetes](https://github.com/kubernetes/kubernetes), E2B
