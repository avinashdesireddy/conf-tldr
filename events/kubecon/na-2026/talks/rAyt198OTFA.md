# Lessons Learned Sandboxing Agents with kagent

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Peter Jausovec (Solo.io), Nina Polshakova (Solo.io), Eitan Yarmush (Solo.io)  
**Video:** [YouTube](https://www.youtube.com/watch?v=rAyt198OTFA) (29:33)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Lessons+Learned+Sandboxing+Agents+with+kagent)  
**Tags:** `agent-security`, `sandboxes`, `kagent`, `agent-substrate`, `isolation`

> Solo.io engineers tried a pod per agent, Anthropic's sandbox runtime, Agent Sandbox and NVIDIA OpenShell, and found each solved only part of the problem, so they joined Google's Agent Substrate and rebuilt kagent 1.0 on it. Their main lessons: isolation is table stakes, and the hard parts are suspend and resume, keeping all controls outside the agent, identity that follows the session, and treating snapshots as sensitive data.

## Key points

- An agent needs compute, identity, networking and storage like any workload, but sessions last hours, are stateful, mostly idle, and the agent can do anything a user can. [1:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=60s)
- A sandbox defines what an agent can see, touch, call and persist: file system, network, tools, credentials, identity, and cleanup between sessions. [2:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=120s)
- A homegrown pod per agent gave Kubernetes identity, policy and observability, but no real sandbox. [3:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=180s)
- Anthropic's sandbox runtime (bubblewrap on Linux, sandbox-exec on macOS, domain-allowlist proxy) suits laptops but meant many sandbox processes inside kagent pods, with no per-agent identity, a shared host kernel, and the proxy inside the sandbox. [4:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=240s)
- Agent Sandbox gave a stateful pod under gVisor or Kata with sub-second warm pools, but idle agents still held CPU and memory and identity stayed with the pod. [6:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=360s)
- NVIDIA OpenShell denied egress by default with per-binary rules and swapped placeholder credentials for real keys at the proxy, but still ran one always-on sandbox per agent with enforcement inside it. [7:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=420s)
- Agent Substrate snapshots idle actors to object storage, restores them in milliseconds, keeps the Kubernetes API off the hot path, and is default-deny with no keys inside. [9:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=540s)
- kagent 1.0 is rebuilt on Agent Substrate: a harness (owned by infra), an agent template, and an agent binding them, compiled into an actor template; each session becomes an actor reachable over A2A, MCP or gRPC. [11:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=660s)
- A new sandbox template resource defines the OCI image, preloaded directories, git repos and skills; one user's agents began sharing state through a common sandbox file system on their own. [16:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=960s)
- Lessons: all controls live outside the agent, identity follows the actor not the pod, suspended agents are stored data that need encryption, retention and restore rules, and the sandbox runtime becomes part of the snapshot format. [18:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=1080s)
- Demo: Anthropic-hosted managed agents run sessions in kagent sandboxes on your cluster; file systems are isolated per session and egress is denied until a policy is applied at runtime. [22:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=1320s)

## Numbers stated

- Agent Sandbox warm pools start a pod in under a second. [6:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=360s)
- Agent Substrate restores actors from snapshots in milliseconds, versus seconds for pods. [9:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=540s)

## Open gaps

- kagent has not enabled memory snapshots because of their complexity, and the runtime-specific snapshot format needs to be hidden from most users. [20:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=1200s)
- Managed-agent support (provider-hosted loop, local sandboxes) is experimental and on main only; the team wants feedback on whether it belongs in kagent core. [22:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=1320s)
- Snapshotting GPU state so inference can run inside the same actors is still being worked on. [28:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=1680s)
- Agents sharing a sandbox file system to talk to each other was an emergent, probably insecure behavior. [17:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=1020s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| learn | Compare where egress and credential enforcement live in Anthropic's sandbox runtime, OpenShell, Agent Sandbox and Agent Substrate. | [4:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=240s) |
| build | Encrypt agent snapshot buckets and define retention and who may restore a session. | [20:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=1200s) |
| contribute | Try the experimental managed-agent support in kagent main and report whether it should be in core. | [22:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=1320s) |
| build | Define kagent sandbox templates with default-deny egress and add allow rules dynamically per agent. | [26:00](https://www.youtube.com/watch?v=rAyt198OTFA&t=1560s) |

## Projects mentioned

kagent, Agent Substrate, [Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox), [gVisor](https://github.com/gvisor/gvisor), Kata Containers, NVIDIA OpenShell, Anthropic Sandbox Runtime, [Kubernetes](https://github.com/kubernetes/kubernetes), Model Context Protocol, A2A
