# Follow the GPUs: How a Regulated Fortune 100 Serves Customers When No Single Cloud Has Enough

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Michael Kinsley (GEICO), Yuva Peavler (GEICO)  
**Video:** [YouTube](https://www.youtube.com/watch?v=71NwaH0y5OM) (34:36)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Follow+the+GPUs%3A+How+a+Regulated+Fortune+100+Serves+Customers+When+No+Single+Cloud+Has+Enough)  
**Tags:** `gpu-scheduling`, `multi-cloud`, `workload-identity`, `capacity-planning`, `zero-trust`

> GEICO runs a hybrid cloud fabric (flat L3 network, identical clusters, SPIFFE/SPIRE identity, Istio and Cilium) that makes moving a workload between Azure and AWS just a redeploy. They built a probe tool that measured GPU availability across providers for four weeks and found multi-region helps only for scarce SKUs, and propose a capacity booking agent since autoscalers never buy capacity.

## Key points

- Takeaways first: for current single-GPU SKUs right now, support multi-region; for 8-GPU flagship nodes, book ahead; and someone still has to do the booking, because autoscalers will not. [1:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=60s)
- The fabric was built for other reasons: four nines across 50 states, replacing about a thousand team-owned clusters and over a million firewall rules with a provider-agnostic zero-trust overlay. [3:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=180s)
- Foundation: one flat L3 network with routable node and pod IPs across providers; identical clusters from immutable hardened images, kubeadm and Ansible, with components on the same versions and delivered by GitOps. [3:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=180s)
- SPIRE issues SPIFFE IDs and short-lived SVIDs from attested evidence; Istio sidecars enforce mTLS with certs from the SPIRE agent; Cilium enforces deny-by-default L3/L4 policy. [5:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=300s)
- Teams describe apps and their communication; the platform generates Cilium and Istio policy, with automatic approval for most rules and human review for risky ones. [7:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=420s)
- The control plane runs active-active in three regions on Cassandra, which also backs a SPIRE fork with a pluggable datastore proposed upstream; Kafka is the fleet bus, and a mesh agent syncs endpoints and policy to each cluster. [8:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=480s)
- Because identity and rules attach to what a workload is, not where it runs, moving from Azure to AWS is a redeploy with the same global name and no client changes. [10:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=600s)
- Providers now offer bookable capacity (e.g. AWS capacity blocks, up to 8 weeks out, paid up front, no refunds) between on-demand and reserved; Karpenter will use a reservation ID but never buys one. [15:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=900s)
- The 'follow the GPUs' tool doubles its GPU request until refused, with Blackbox Exporter-style probe config, free probes (spot score and price) and billable catch-and-release probes, telemetry in S3/Blob queried with DuckDB, and a scheduled sweeper as an emergency brake. [16:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=960s)
- Results: small single-GPU SKUs gain nothing from multi-region, L40S gains about 5%, sparse RTX Pro 6000 gains a lot, and B200 is not available on demand but multi-region raises odds of getting one within two days. [22:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=1320s)
- Q&A: multi-cluster autoscaling approaches still just wait and retry when refused; Azure model-as-a-service by data zone plus an AI gateway can soften shortages; NVIDIA Dynamo intent CRs are scoped to one cluster. [28:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=1680s)

## Numbers stated

- About 1,000 Kubernetes clusters and over 1 million firewall rules in the old model. [3:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=180s)
- Control plane runs in three regions, all active. [8:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=480s)
- Inference cost for the same capability drops roughly 10x per year (cited from Guido Appenzeller), so 100x in two years. [13:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=780s)
- Capacity can be booked up to 8 weeks ahead. [15:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=900s)
- A catch-and-release probe took about 30 seconds to 2 minutes per VM. [19:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=1140s)
- Ran about four weeks across every zone of three AWS regions and nine Azure regions, collecting about 50,000 samples. [20:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=1200s)
- L40S: about 5% improvement from multi-region; RTX Pro 6000: from about 45% to 70-75%. [22:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=1320s)
- B200: chance of getting capacity within two days rose from about 65% to 88%. [23:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=1380s)

## Open gaps

- No autoscaler books capacity; when the provider says no they can only wait and retry. GEICO proposes a booking agent with an interface for need, timing and budget, informed by history. [24:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=1440s)
- The booking agent and multi-cluster placement layer do not exist yet; they are still checking whether it would help. [31:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=1860s)
- Data gravity constrains where many workloads can run. [32:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=1920s)
- Securing agents with workload identity is unsolved; sidecar credential injection is the direction, but no full answer yet. [33:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=1980s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Run GEICO's shared probe tool in your own accounts to measure GPU SKU availability by region before committing to multi-region. | [26:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=1560s) |
| contribute | Help define the interface for a GPU capacity booking agent that reserves capacity just before pods go pending. | [26:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=1560s) |
| contribute | Review the SPIRE pluggable datastore proposal and the Cassandra-backed implementation. | [9:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=540s) |
| learn | Identity-based (SPIFFE) network policy that lets workloads move across clouds without rewriting rules. | [10:00](https://www.youtube.com/watch?v=71NwaH0y5OM&t=600s) |

## Projects mentioned

SPIFFE, SPIRE, [Istio](https://github.com/istio/istio), Cilium, Envoy, Cassandra, Kafka, kubeadm, Ansible, Karpenter, Blackbox Exporter, DuckDB, [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo), Dragonfly, [Kubernetes](https://github.com/kubernetes/kubernetes)
