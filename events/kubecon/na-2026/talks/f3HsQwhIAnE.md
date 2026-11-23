# Fireside Chat: Future of Kubernetes and Agents with Tim Hockin and Kelsey Hightower

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Tim Hockin (Google), Kelsey Hightower, Savannah Peterson  
**Video:** [YouTube](https://www.youtube.com/watch?v=f3HsQwhIAnE) (27:49)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Fireside+Chat%3A+Future+of+Kubernetes+and+Agents+with+Tim+Hockin+and+Kelsey+Hightower)  
**Tags:** `agents`, `kubernetes`, `agent-security`, `platform-engineering`, `agent-identity`

> Savannah Peterson hosts Tim Hockin and Kelsey Hightower on why agents need a different platform layer: they are untrusted, mostly idle and single-tenant, which normal Kubernetes patterns serve with poor startup times or poor utilization. They frame Agent Substrate as Kubernetes extended for a new workload, urge teams to check they need an agent at all, and name delegated identity and permission scoping as open problems.

## Key points

- Hightower: an agent differs from a shell script in taking unstructured input and making its own decisions; the work is limiting it to only the problem you asked it to solve. [2:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=120s)
- Hockin: agents are untrusted ("malware in a box") so must be sandboxed, spend most of their life asleep waiting for input, and are single-tenant. [4:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=240s)
- Together these give either poor user experience from repeated startups or single-digit cluster CPU utilization; Agent Substrate aims to fix both on Kubernetes. [5:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=300s)
- Hightower: new workloads reshape the platform, as microservices forced observability; Knative and Istio are earlier examples of building a workload platform on Kubernetes. [6:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=360s)
- A 2 to 4 second container start is fine for services that run for weeks, but not for an agent that works 500 ms and sleeps again. [8:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=480s)
- Hightower: most of Agent Substrate's technology already existed; it is packaged for this workload. [10:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=600s)
- Security defaults: sandboxing cannot be turned off, agents have no network without permission, egress goes to a pluggable policy enforcement point, and every agent has its own identity. [11:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=660s)
- Advice: start small and try it on something unimportant (Hockin); first confirm the task needs an agent, recalling how serverless functions grew into VMs (Hightower). [14:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=840s)
- Per-team clusters or central control: teams that already run clusters can try it; otherwise use a dedicated node pool or dedicated cluster, partly because Substrate needs a recent Kubernetes version. [18:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=1080s)
- On-behalf-of identity: v1 has its own identity and issuer; down-scoped user identity (OBO) is being discussed with users and is not done. [21:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=1260s)
- For an SRE agent, give it only the tools, data sources and network paths the on-call human uses, and constrain it with skill files. [25:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=1500s)

## Numbers stated

- Container start of 2 to 4 seconds versus an agent run of about 500 ms. [8:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=480s)
- People have used agents in earnest for about a year and a half. [7:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=420s)
- Audience show of hands: roughly 50/50 between actively building with AI and wanting to start. [13:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=780s)

## Open gaps

- Carrying a user's identity through agents with down-scoped on-behalf-of tokens is not done yet in Agent Substrate. [21:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=1260s)
- Open-ended agents push teams to grant broad permissions up front; scoping permissions for tasks you cannot predict is unsolved. [22:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=1320s)
- v1 will not fit everyone: users are asking for bring-your-own identity and new network and other policies. [12:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=720s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| learn | Try Agent Substrate on a non-critical workload in a test cluster, ideally on a dedicated node pool. | [14:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=840s) |
| build | Scope an SRE agent's sandbox to the exact tools and network paths an on-call engineer needs, and nothing else. | [26:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=1560s) |
| contribute | Give the project feedback on identity needs such as on-behalf-of flows and bring-your-own identity. | [21:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=1260s) |
| write | Map which of your automation tasks need an agent and which should stay fixed-behavior scripts. | [15:00](https://www.youtube.com/watch?v=f3HsQwhIAnE&t=900s) |

## Projects mentioned

Agent Substrate, [Kubernetes](https://github.com/kubernetes/kubernetes), Knative, [Istio](https://github.com/istio/istio), Docker
