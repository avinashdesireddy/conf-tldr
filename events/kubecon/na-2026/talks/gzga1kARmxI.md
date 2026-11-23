# Pods Are Not Enough for AI Agents, Meet Agent-substrate

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Christian Posta (Solo.io)  
**Video:** [YouTube](https://www.youtube.com/watch?v=gzga1kARmxI) (30:53)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Pods+Are+Not+Enough+for+AI+Agents%2C+Meet+Agent-substrate)  
**Tags:** `agents`, `agent-sandboxing`, `agent-security`, `credential-brokering`, `kubernetes`

> Christian Posta argues that agents break microservice assumptions: they run unknown code, hold state and sit idle, so a session per pod overloads Kubernetes. Agent Substrate decouples actors from worker pods, snapshots idle actors to storage, wakes them on request, and forces all egress through policy with credential injection; kagent supplies the agent-aware layer on top.

## Key points

- Microservice assumptions (known code, stateless replicas, many users per pod, pods running hot) do not hold for agents, which write and run untested code, accumulate state and wait for humans or events. [2:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=120s)
- Running one sandboxed pod per session, plus short-lived tool sandboxes, creates far more objects than the Kubernetes API server is built for. [7:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=420s)
- Agent Substrate decouples a session (actor) from compute; actor state lives in Substrate's own control plane, not in Kubernetes custom resources. [8:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=480s)
- Kubernetes still runs the compute: a WorkerPool custom resource defines worker pods, volumes and sandbox class, while actor templates and actors are Substrate objects. [9:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=540s)
- Idle actors are snapshotted out of workers and rehydrated on any worker; identity is durable across the actor's life, and a request to a paused actor triggers activation through the router. [10:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=600s)
- Snapshot level is configurable: root FS only, root FS plus workspace (durable directory), or those plus memory. Snapshots go to pluggable S3-compatible or GCS storage, with state in Postgres. [16:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=960s)
- Demo: three actors from one template; two fill a single worker, one is suspended to make room, and scaling workers from one to two lets a router call wake the third. [13:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=780s)
- Actors run in gVisor or microVM sandboxes and are treated as hostile: DNS, UDP and TCP egress is blocked unless a policy allows it. [21:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=1260s)
- Credential brokering: the actor sends a placeholder and agentgateway on the egress path injects the real token from OpenBao, so the agent never holds the secret. [22:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=1320s)
- Pod workload identity cannot tell apart actors sharing a pod; an identity policy adds a per-actor JWT so the destination can attribute the call. [24:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=1440s)
- Substrate knows nothing about agents, MCP or conversations; kagent (1.0 this week) decides when to snapshot and handles agent revisions and rollouts. [28:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=1680s)

## Numbers stated

- Control plane target: hundreds of millions, up to a billion object changes per cluster. [9:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=540s)
- North Star: a billion actors per cluster and activation in 100 ms or less. [29:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=1740s)
- Solo.io and Google started collaborating on Agent Substrate around April or May. [1:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=60s)

## Open gaps

- Substrate can snapshot on command, but knowing when to pause an actor needs an agent-aware layer above it. [29:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=1740s)
- Without an actor identity policy, the destination only sees a shared bot token and cannot attribute calls to an actor. [27:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=1620s)
- Harnesses keep leaking bearer credentials placed inside agents, which pushes teams to broker credentials outside the sandbox. [23:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=1380s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Broker agent credentials on the egress path (placeholder in, real token injected from a vault) instead of putting API keys in the sandbox. | [26:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=1560s) |
| contribute | Write a Substrate storage or credential-provider plugin; storage is pluggable outside the main tree. | [17:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=1020s) |
| learn | Use the Substrate calculator on kagent.dev to compare actor density and idle-pod cost for your workloads. | [30:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=1800s) |
| learn | Read the agentgateway blog series on credential brokering and blast radius. | [23:00](https://www.youtube.com/watch?v=gzga1kARmxI&t=1380s) |

## Projects mentioned

Agent Substrate, kagent, [agentgateway](https://github.com/agentgateway/agentgateway), [gVisor](https://github.com/gvisor/gvisor), OpenBao, PostgreSQL, [Kubernetes](https://github.com/kubernetes/kubernetes), Claude Code, OpenClaw
