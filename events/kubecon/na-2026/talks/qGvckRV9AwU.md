# Why Are You Still Wasting Whole GPUs? Hardware-Level Sharing, Scheduled with DRA

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Engin Diri (Pulumi)  
**Video:** [YouTube](https://www.youtube.com/watch?v=qGvckRV9AwU) (30:12)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Why+Are+You+Still+Wasting+Whole+GPUs%3F+Hardware-Level+Sharing%2C+Scheduled+with+DRA)  
**Tags:** `gpu-sharing`, `dra`, `mig`, `ai-inference`, `platform-engineering`

> A Pulumi solutions architect describes building a self-hosted inference platform for a European customer that splits GPUs into NVIDIA MIG slices and schedules them with Dynamic Resource Allocation (DRA). MIG gives the isolation time-slicing lacks, and DRA lets workloads ask for slices by attributes, but quotas, large models and chargeback remain open.

## Key points

- European customers want to self-host models for control and regulation; the speaker's view is that owning the model is easy and using the GPU well is hard. [6:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=360s)
- Option one, one whole GPU per pod via the device plugin with vLLM, showed low utilization in Prometheus while the full card was paid for. [7:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=420s)
- Option two, time-slicing, has no memory or fault isolation, so noisy neighbors hurt workloads; MPS has the same issue. [8:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=480s)
- MIG gives slices with dedicated memory and cache and fault isolation between them; the number of slices depends on the card. [10:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=600s)
- DRA mirrors the storage pattern (DeviceClass like StorageClass, claims like PVCs) and selects devices by attributes with CEL. [12:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=720s)
- A shared ResourceClaim lets pods in a namespace share a device; a ResourceClaimTemplate gives each pod its own device matching a CEL selector. [13:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=780s)
- The stack uses the NVIDIA DRA driver, which publishes MIG profiles as ResourceSlices, plus the Gateway API inference extension and agentgateway, which route by backend load instead of kube-proxy's blind balancing. [16:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=960s)
- Demo on an AWS RTX instance: 1g, 2g and 4g MIG profiles exposed as slices; a Qwen3 server and a training pod each got their own slice, queried through an OpenAI-compatible endpoint. [22:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=1320s)
- Rule of thumb: MIG for multiple tenants on one card, latency targets, or training and serving together; time-slicing is still fine for one trusted team, dev boxes and bursty jobs. [27:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=1620s)
- Rollout lessons: pick slice layouts per node pool, label pools with the MIG config, name slices clearly, and start DRA only after MIG is configured to avoid race conditions. [27:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=1620s)
- Guardrails at two points: policy as code in Pulumi before apply, and the same policy in Kyverno at the API server. [28:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=1680s)

## Numbers stated

- MIG slice counts cited: seven on larger data-center cards, four on the RTX card used in the demo. [11:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=660s)
- A consumer RTX gaming GPU was quoted at about 9,000 euros. [9:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=540s)

## Open gaps

- Day-two questions are still open: MIG quota and ordering (a queue such as Kueue), group-shared claims in 1.37, admission policies, and llm-d as the next layer. [24:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=1440s)
- Models larger than a slice or a node need multi-node serving (LeaderWorkerSet is being evaluated); MoE models with prefill and decode pools still need investigation. [25:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=1500s)
- Chargeback to teams by slice-hours is the next big step and not yet built. [28:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=1680s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Recreate the stack on one MIG-capable node: GPU driver, DRA driver, MIG profiles, and two workloads on separate slices behind an inference gateway. | [21:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=1260s) |
| build | Build slice-hour chargeback for MIG slices allocated through DRA. | [28:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=1680s) |
| write | Write a decision guide for MIG vs time-slicing vs MPS based on tenancy, isolation and burstiness. | [27:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=1620s) |
| learn | Enforce GPU request policies both in CI and at the API server with Kyverno, so direct API access cannot bypass them. | [29:00](https://www.youtube.com/watch?v=qGvckRV9AwU&t=1740s) |

## Projects mentioned

[Kubernetes](https://github.com/kubernetes/kubernetes), Dynamic Resource Allocation (DRA), NVIDIA DRA Driver for GPUs, [vLLM](https://github.com/vllm-project/vllm), [llm-d](https://github.com/llm-d/llm-d), [Gateway API](https://github.com/kubernetes-sigs/gateway-api), [Gateway API Inference Extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension), [agentgateway](https://github.com/agentgateway/agentgateway), [Prometheus](https://github.com/prometheus/prometheus), Kyverno, Pulumi, Backstage, [Kueue](https://github.com/kubernetes-sigs/kueue), [LeaderWorkerSet](https://github.com/kubernetes-sigs/lws), NVIDIA Grove
