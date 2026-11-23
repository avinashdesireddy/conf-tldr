# Zero-Gap GPU Execution: Building Secure, Pre-Warmed Pod Runtimes for High-Velocity AI Agents

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Ankit Goyal (LinkedIn), Cong Gu (LinkedIn)  
**Video:** [YouTube](https://www.youtube.com/watch?v=j0kV0TekF3c) (31:45)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Zero-Gap+GPU+Execution%3A+Building+Secure%2C+Pre-Warmed+Pod+Runtimes+for+High-Velocity+AI+Agents)  
**Tags:** `agents`, `gpu-scheduling`, `warm-pools`, `sandboxing`, `volcano`

> LinkedIn built Firepool, a broker that keeps warm GPU pods ready so agents and RL loops running on CPU nodes can launch GPU jobs without Kubernetes pod startup in the critical path. Its zero-gap mode uses HAMi and Volcano to park standby pods on a busy GPU so the next job takes over the card the moment the current one ends.

## Key points

- Motivating workloads: Autopilot (an agent migrating TensorFlow models to PyTorch for tens of hours), an auto-research agent running experiments for days, and agentic RL rollouts. All need GPUs repeatedly but not continuously. [0:00](https://www.youtube.com/watch?v=j0kV0TekF3c)
- Running agents on GPU nodes wastes GPUs while they think; running them on CPU nodes and launching a GPU pod per step pays a cold start every iteration. [4:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=240s)
- The Firepool broker has a REST API, job store and pool controller for capacity, plus a dispatcher, in-memory pod tracker and executors; each pod runs a lightweight Firepool agent that fetches and runs the job code. [7:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=420s)
- The API is built for agents: submit returns a job ID immediately, unknown fields are rejected to block hallucinated input, retries stay under one job ID, and failures return a specific error class and exit code. [9:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=540s)
- Pod selection order: the caller's own idle pod, then a never-used idle pod, then a standby on a busy GPU, and only last a new pod. Claiming happens in one step under one lock; multi-pod jobs claim all pods at once, gang-style. [10:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=600s)
- Pods start with a shared base image (CUDA, framework); user code, extra Python packages and distributed rank/addresses arrive with the job, so one pool serves many environments. [13:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=780s)
- Safe reuse rules: verified reset of the process tree, code and shared memory (else delete the pod), owner-only reuse, and a reuse tag that marks a pod for retirement when a different tag lands on it. [14:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=840s)
- Pools are sized from the job queue, not GPU utilization, with four knobs: floor, ceiling, idle wait time, and idle pods kept after that. Firepool can borrow idle GPUs from other teams and return them on demand. [16:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=960s)
- Zero gap uses HAMi only for scheduling multiple pods per GPU (no partitioning or time sharing); one pod runs a job with the full card while standby pods wait to be promoted. [19:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=1140s)
- Sandboxing: pods have no egress by default; all outbound traffic goes through a sidecar proxy that holds the credentials, injects them and checks policy. A checkpoint daemon persists agent state, and shared memory lets agent instances share learnings. [22:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=1320s)
- Q&A: Firepool only uses spare capacity and does not run production training; fragmentation is handled with fixed GPU SKU types and custom Volcano bin-packing plugins. [26:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=1560s)

## Numbers stated

- New GPU pod cold start with cached image: 20-30 seconds; uncached image: 2-10 minutes. [5:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=300s)
- Binding a job to a warm pod takes under half a second. [13:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=780s)
- Median handover time with a different reuse tag per job dropped from 51 seconds to under a second. [21:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=1260s)
- A new GPU pod takes about 22 seconds to run its first instruction; on a warm pod job code starts in about a second. [24:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=1440s)
- In an H200 benchmark, an agent loop went from 26 minutes to 2. [24:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=1440s)
- 19 of 20 pod requests in production are served from warm pods (standbys included). [24:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=1440s)
- Auto-research agent runs have lasted 7 days. [3:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=180s)
- Autopilot cut TensorFlow-to-PyTorch migration time per model from months to about a week. [27:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=1620s)

## Open gaps

- Standby pods with different container images on the same GPU are not supported yet; it is the next step, aimed at many RL environments on a small GPU budget. [21:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=1260s)
- When the cluster is full, plain warm pools cannot grow and jobs wait for capacity again; agents now mostly wait on quota rather than cold start. [17:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=1020s)
- Pod reuse is not a security boundary: state outside tracked writable paths is handled by read-only pods and opt-out, not full isolation. [30:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=1800s)
- Firepool is not open source yet; the team plans to release it. [25:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=1500s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Add a warm-pod broker in front of GPU jobs for agent loops, sized from queue depth with floor and ceiling knobs. | [16:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=960s) |
| build | Use HAMi scheduling slots with Volcano to park standby pods on busy GPUs and cut handover gaps between tenants. | [19:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=1140s) |
| contribute | Follow Firepool's planned open-source release and help with multi-image standby support. | [25:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=1500s) |
| learn | Sidecar credential injection with no-egress pods as a pattern for running untrusted agent code. | [22:00](https://www.youtube.com/watch?v=j0kV0TekF3c&t=1320s) |

## Projects mentioned

Firepool, [Volcano](https://github.com/volcano-sh/volcano), [HAMi](https://github.com/Project-HAMi/HAMi), [Kubernetes](https://github.com/kubernetes/kubernetes), PyTorch, TensorFlow
