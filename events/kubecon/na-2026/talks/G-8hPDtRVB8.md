# Kubernetes Solutions for Agent-Shaped Problems

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Tim Hockin (Google), Dmitry Berkovich (Google)  
**Video:** [YouTube](https://www.youtube.com/watch?v=G-8hPDtRVB8) (38:24)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Kubernetes+Solutions+for+Agent-Shaped+Problems)  
**Tags:** `agents`, `agent-sandboxing`, `kubernetes`, `snapshots`, `agent-security`

> Tim Hockin and Dmitry Berkovich explain why the obvious pod-per-agent-session pattern on Kubernetes gives slow starts and poor utilization, and how Agent Substrate fixes it with secure-by-default sandboxes, near-zero cost for idle agents and fast wake from layered snapshots. The long Q&A covers the policy enforcement point, snapshot invalidation and missing pieces such as autoscaling and automatic suspend.

## Key points

- Agent workloads are bursty (work for 100 ms to half a minute, then idle for hours), run untrusted generated code that needs full isolation, and have a human waiting for responses. [1:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=60s)
- Pod per session wastes requested resources while the user thinks, then destroys the pod on timeout and pays the slow sandbox start again on return. [3:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=180s)
- Teams that rolled their own ran many sandboxes inside large pods, then needed a control plane across nodes, effectively rebuilding Kubernetes. [5:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=300s)
- Three principles: security (no network by default, everything sandboxed, per-agent identity), density (idle agents cost about zero) and speed (wake feels like it never slept). [6:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=360s)
- Built on Kubernetes: workers are pods, the control plane and policy run in the cluster, and on node drain workers move their agents elsewhere. [8:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=480s)
- Concepts: actor (one session), actor template, worker (a pod hosting many actors), outlet (per-node manager handling images and snapshots), and ATE net with a router and an egress. [9:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=540s)
- Actors have no IP; the router finds the actor from the DNS name, holds the request while it resumes the actor, and the egress applies policy and injects credentials. [11:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=660s)
- Snapshots have layers: OCI image, a mandatory volume, root FS diffs and memory. Same image and machine type allows a full resume; a new image throws away memory and root FS for a cold start from the volume. [12:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=720s)
- Common pattern: a managed agent loop such as Gemini (brains) calls Substrate inside your own perimeter (hands), where work can be audited and stopped. [15:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=900s)
- The policy enforcement point is a plug-in: actor traffic is wrapped in HTTP CONNECT and sent to it; Envoy and Solo.io's agentgateway are the two implementations so far. [17:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=1020s)
- Suspend writes a local snapshot, then uploads it asynchronously; the scheduler prefers a node that still holds the latest copy. Only the durable directory is guaranteed to persist. [22:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=1320s)

## Numbers stated

- Sandbox pod startups seen at 15 seconds, 30 seconds and up to a couple of minutes. [3:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=180s)
- Aspirational goals: billions of agents in one cluster, 10,000+ activations per second, wake in about 100 ms. [7:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=420s)
- In 1.0, snapshot upload to cloud storage starts after 5 minutes suspended. [23:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=1380s)
- Users have been in production since 0.2, released two months ago; the project has been built for about 6 months. [20:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=1200s)

## Open gaps

- No good autoscaling story for worker pods and nodes; HPA on CPU and memory does not fit agents that sleep and wake often, so sizing is manual today. [19:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=1140s)
- Memory management is imperfect: no in-place resource updates, and a hostile workload can still exhaust memory. [22:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=1320s)
- Suspend is manual or harness-driven; detecting idleness automatically is unsolved, and self-suspend is coming. [24:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=1440s)
- Base image patches invalidate memory and root FS snapshots for every affected actor; merging overlays is an open question. [29:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=1740s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| contribute | Write a third policy enforcement point implementation for Substrate egress. | [18:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=1080s) |
| build | Design autoscaling signals for Substrate worker pools from activation and suspend activity rather than CPU. | [19:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=1140s) |
| build | Make your agent harness call suspend when a task finishes, and keep needed state in the durable directory. | [24:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=1440s) |
| learn | The brains/hands split for running managed agent loops against compute inside your own security perimeter. | [15:00](https://www.youtube.com/watch?v=G-8hPDtRVB8&t=900s) |

## Projects mentioned

Agent Substrate, [Kubernetes](https://github.com/kubernetes/kubernetes), [gVisor](https://github.com/gvisor/gvisor), Cloud Hypervisor, Envoy, [agentgateway](https://github.com/agentgateway/agentgateway), Gemini
