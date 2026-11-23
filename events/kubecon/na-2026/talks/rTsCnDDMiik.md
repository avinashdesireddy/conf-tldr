# Platform-First AI Agent Security: Zero-Trust Patterns for Kubernetes

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Carlos Santana (AWS)  
**Video:** [YouTube](https://www.youtube.com/watch?v=rTsCnDDMiik) (27:50)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Platform-First+AI+Agent+Security%3A+Zero-Trust+Patterns+for+Kubernetes)  
**Tags:** `agent-security`, `zero-trust`, `sandboxes`, `platform-engineering`, `kro`

> Carlos Santana argues platform teams should treat AI agents as untrusted tenants and layer identity, policy and isolation around them using CNCF projects. He shows KRO compositions that stamp out agent workloads, egress policies and Agent Substrate worker pools per namespace, plus Agent Sandbox warm pools, OpenShell with Cedar policies, and credential proxies.

## Key points

- Enterprise interest in agent security is driven by insecure agent use and incidents where agents reach systems they should not, not by productivity. [1:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=60s)
- Treat agents as tenants running untrusted, LLM-generated code; the three concerns are identity, policy and isolation. [4:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=240s)
- Identity has two cases: an agent acting for an interactive user (token exchange) and an agent running overnight without the user; SPIFFE/SPIRE gives agents a URI identity tied to a JWT or X.509 certificate. [4:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=240s)
- Policy covers what an agent may run and read, including layer 7 paths, plus temporal rules (e.g. deny after five executions) via Dogwood, an AWS project built on Cedar, using audit logs of agent sessions. [6:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=360s)
- A KRO resource graph definition declares a CRD and its controller in YAML with CEL, so platform teams can define an AgentWorkload with a narrow prompt and allowed FQDNs without writing Go. [9:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=540s)
- The AgentWorkload composes an egress policy, an agent template and an agent, the kagent abstractions now built on Agent Substrate; KRO infers creation order from references. [11:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=660s)
- A new experimental KRO graph mode creates a worker pool, harness, service account and quota in any namespace labeled as a tenant; resource quotas can cap custom resources such as agents. [15:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=900s)
- Owning your own platform APIs shields consumers from breaking changes in fast-moving agent projects. [18:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=1080s)
- Isolation levels: gVisor syscall emulation, VM isolation with Kata Containers, and hardware isolation with the newly announced AWS Nitro Sandboxes on EKS. [19:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=1140s)
- Agent Sandbox warm pools with claims (like PVCs) hand out a ready sandbox instantly and backfill the pool. [20:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=1200s)
- OpenShell restricts which files and binaries an agent can use; an open PR proposes Cedar as its policy language, e.g. allowing GitHub access only through one binary. Secrets are injected by a credential proxy, never given to the agent. [23:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=1380s)

## Numbers stated

- Launching a micro VM takes three to four seconds, plus a couple of seconds for the image. [20:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=1200s)
- A claim against a warm pool returns a sandbox in under a second. [21:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=1260s)
- The KRO graph feature arrived this week in KRO 0.10 and is experimental. [15:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=900s)

## Open gaps

- Cedar as OpenShell's policy language is still an open proposal and PR, not merged. [24:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=1440s)
- The KRO graph mode is experimental and needs user feedback. [15:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=900s)
- Handling permissions for agents that run overnight without the user is an open identity question. [5:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=300s)
- Agent behavior cannot be pinpointed in advance, so policy must describe expected behavior rather than exact actions. [7:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=420s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Define a KRO-based AgentWorkload API that bundles egress policy, agent template and quota, so teams consume a stable platform interface. | [13:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=780s) |
| build | Put a credential proxy in front of agents that injects secrets into outbound requests instead of mounting them. | [25:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=1500s) |
| contribute | Review the Cedar policy proposal for OpenShell and give feedback on KRO's experimental graph mode. | [24:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=1440s) |
| learn | Compare gVisor, Kata Containers and hardware-isolated micro VMs for running untrusted agent code. | [19:00](https://www.youtube.com/watch?v=rTsCnDDMiik&t=1140s) |

## Projects mentioned

[Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox), KRO, kagent, Agent Substrate, [gVisor](https://github.com/gvisor/gvisor), Kata Containers, NVIDIA OpenShell, Cedar, Dogwood, SPIFFE, SPIRE, Cilium, Amazon EKS, AWS Nitro Sandboxes, [Kubernetes](https://github.com/kubernetes/kubernetes), containerd, Helm, [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-collector)
