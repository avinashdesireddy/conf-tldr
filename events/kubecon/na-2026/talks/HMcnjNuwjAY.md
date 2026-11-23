# Your Peers Are Struggling With LLM Inference on Kubernetes Too. Here's What the Data Says

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Danielle Cook (Akamai), Andy Suderman (Fairwinds)  
**Video:** [YouTube](https://www.youtube.com/watch?v=HMcnjNuwjAY) (24:06)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Your+Peers+Are+Struggling+With+LLM+Inference+on+Kubernetes+Too.+Here%27s+What+the+Data+Says)  
**Tags:** `ai-inference`, `survey-data`, `autoscaling`, `routing`, `platform-engineering`

> Using an Akamai-commissioned survey of 200 practitioners running AI in production, plus CNCF, Forrester and Cast AI data, the speakers show that most teams struggle with latency at peak, GPU capacity and routing. They map the failure points across scheduling, scaling, networking and ownership, and close with five steps to production inference on Kubernetes.

## Key points

- The top blocker to running inference close to users is tooling and platform maturity, ahead of cost uncertainty, security, data handling and observability. [2:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=120s)
- Kubernetes is the default for AI workloads; the problem is complexity and speed, since few organizations deploy their generative AI stack daily. [3:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=180s)
- Expectations are strict: sub-500 ms end-to-end responses, tail-latency measurement (P95/P99), and rollback within an hour when inference performance degrades. [4:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=240s)
- Scheduling: set resource requests, use DRA and Kueue to share GPUs, watch GPU splitting, right-size the CPU-heavy parts too, and measure utilization and latency. [8:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=480s)
- Scaling: startup is slow (instance plus model load), so do not scale on CPU; scale on latency and time to first token using vLLM metrics with KEDA. [10:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=600s)
- Routing: replicas each hold their own KV cache, so generic load balancing wastes cache; route on cache contents, queue depth and load with Gateway API Inference Extension, llm-d or KServe. [12:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=720s)
- Teams say proximity to users is critical, but planned architectures stay flat: single-region stays about the same and multi-region slightly declines. You cannot autoscale past the speed of light. [15:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=900s)
- Ownership is the hardest part: inference probably belongs to the platform team, but SLOs like time to first token and token cost need clear owners. [17:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=1020s)
- A maturity grid (getting started, scaling, leading) covers placement, autoscaling signals and routing, mapped to the CNCF Cloud Native Maturity Model. [20:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=1200s)
- Five steps: start from an AI-conformant cluster, cut startup time by caching or streaming weights near the GPU, autoscale on inference signals, add an inference-aware gateway, and set a P95 TTFT SLO with planned rollbacks. [22:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=1320s)

## Numbers stated

- Survey: 200 practitioners all running AI in production, two-thirds engineers. [1:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=60s)
- Nearly 1 in 5 name tooling and platform maturity as the top blocker. [2:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=120s)
- 66% of organizations hosting generative AI use Kubernetes; only 7% deploy that stack daily. [3:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=180s)
- 82% need end-to-end response in 500 ms or less; 64% in 250 ms or less. [4:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=240s)
- 39% measure P95 and 17% P99. [5:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=300s)
- Over 70% need rollback within an hour; nearly half within 15 minutes. [5:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=300s)
- Half name latency at peak load as one of the hardest scaling problems; bursty concurrency 43%; GPU capacity planning 37%. [6:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=360s)
- Average GPU utilization across Kubernetes clusters is 5% (Cast AI data). [8:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=480s)
- On a degrading model: 51% keep the same model, 39% switch to a smaller one, 37% fail over, 12% block the action, 7% have no fallback; 64% call automated traffic steering very important or critical. [12:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=720s)
- After moving to an inference-aware gateway, one user's prefix cache hits doubled from 35% to 70% and TTFT dropped by more than 35% on the same hardware. [14:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=840s)
- 60% say being close to users is critical; single-region plans go from 46% to 45% and multi-region from 22% to 20% over two years. [15:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=900s)
- 47% in the CNCF survey say culture is the biggest blocker. [17:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=1020s)

## Open gaps

- Sharing or splitting GPUs across workloads is still early. [9:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=540s)
- There is no default tooling for inference-aware traffic steering even though teams say it is critical. [13:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=780s)
- Architectures are not moving closer to users despite stricter latency needs. [16:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=960s)
- Ownership of inference SLOs and token cost between platform and app teams is unresolved. [20:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=1200s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Replace CPU-based HPA on inference pods with KEDA scaling on vLLM queue depth, KV cache or TTFT metrics. | [11:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=660s) |
| build | Put an inference-aware gateway (Gateway API Inference Extension or llm-d) in front of model servers and measure prefix cache hit rate. | [23:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=1380s) |
| learn | Place your teams on the getting-started/scaling/leading grid and the CNCF Cloud Native Maturity Model. | [21:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=1260s) |
| write | Define who owns the TTFT SLO and GPU/token cost between platform and application teams. | [20:00](https://www.youtube.com/watch?v=HMcnjNuwjAY&t=1200s) |

## Projects mentioned

[Kubernetes](https://github.com/kubernetes/kubernetes), [Kueue](https://github.com/kubernetes-sigs/kueue), [KEDA](https://github.com/kedacore/keda), [vLLM](https://github.com/vllm-project/vllm), [Gateway API Inference Extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension), [llm-d](https://github.com/llm-d/llm-d), [KServe](https://github.com/kserve/kserve), Goldilocks, Pluto, Dynamic Resource Allocation (DRA), CNCF Cloud Native Maturity Model
