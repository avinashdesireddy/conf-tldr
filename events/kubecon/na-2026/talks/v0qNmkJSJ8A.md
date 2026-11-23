# Clueless About The Cost of AI Model Usage? OpenCost+llm-d = first of a kind inference cost tracking

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Alexander Meijer (IBM), Sima Nadler (IBM)  
**Video:** [YouTube](https://www.youtube.com/watch?v=v0qNmkJSJ8A) (30:08)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Clueless+About+The+Cost+of+AI+Model+Usage%3F+OpenCost%2Bllm-d+%3D+first+of+a+kind+inference+cost+tracking)  
**Tags:** `ai-inference`, `cost`, `finops`, `llm-d`, `gpu-utilization`

> OpenCost now reads llm-d and vLLM token metrics and combines them with provider pricing and DCGM data to report cost per model and per token. A live demo on an IBM research cluster compares allocation and usage cost to expose idle models, and the roadmap targets GPU usage-based allocation, time slicing and richer idle detection.

## Key points

- Self-hosted models are generally cheaper than hosted ones, but that only delays the cost problem as self-hosting grows. [1:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=60s)
- OpenCost, a CNCF incubating FinOps tool, covers Kubernetes, cloud provider and plugin-based SaaS costs via the FOCUS spec, with Parquet exporters, APIs and a UI. [2:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=120s)
- Responsibility split: llm-d handles token counts, routing and scheduling; OpenCost handles pricing, cloud provider connections and metric aggregation, and never runs LLMs. [6:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=360s)
- Outputs include dollars per token and hardware utilization, aimed at cost-aware model routing and comparing self-hosting with hosted APIs. [7:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=420s)
- Allocation cost is the max of request and usage, a production metric that rewards right-sizing; usage cost charges only measured use, an R&D metric that tolerates over-requesting. [12:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=720s)
- Input versus output cost is split using vLLM prefill time versus decode time. [19:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=1140s)
- Demo: the inference-cost totals API aggregated by model and namespace showed a large gap between allocation and usage cost for one model, marking it for right-sizing or more traffic. [20:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=1200s)
- Per-model idle cost is derived from two OpenCost API calls, one sharing idle and shared costs and one keeping them separate, then subtracting. [23:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=1380s)
- Dashboard widgets show cost per million tokens and the most idle and most expensive idle models; many models had no tokens, like abandoned container workloads. [25:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=1500s)

## Numbers stated

- OpenCost launched in 2019 and has about 7,000 GitHub stars. [2:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=120s)
- A CNCF survey found 66% of AI workloads run on Kubernetes. [4:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=240s)
- Worked example: $1 per vCPU-hour, $10 per GPU-hour, $15 total over 150 tokens gives 10 cents per token. [16:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=960s)
- Demo cluster: several dozen llm-d deployments on a few dozen H100 nodes. [17:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=1020s)
- One 120B model over 24 hours: $246 allocation cost ($239 input, $7 output) versus about $22 usage cost. [19:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=1140s)
- That model was idle 90% of the time. [20:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=1200s)
- The most efficient models were only 39% idle; one idle model cost almost $24K over a week. [27:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=1620s)

## Open gaps

- GPU allocation uses only resource requests; usage metrics still need to be folded in, and GPU time slicing is not supported yet. [28:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=1680s)
- Idle detection relies on a single DCGM metric; memory, PCIe and other GPU dimensions are needed to judge fit and right-sizing. [28:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=1680s)
- KV cache settings exist in the API but are not tightly integrated yet. [19:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=1140s)
- OpenCost has no native per-model idle view, so it is computed with a two-call workaround. [23:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=1380s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Use allocation-versus-usage cost per model to find idle or abandoned LLM deployments and right-size them. | [27:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=1620s) |
| contribute | Help OpenCost add GPU time slicing and multi-metric GPU idle detection. | [28:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=1680s) |
| build | Prototype cost-aware model routing that consumes OpenCost cost-per-token metrics. | [7:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=420s) |
| write | Compare self-hosted dollars per token from this integration with hosted API pricing for the same workload. | [11:00](https://www.youtube.com/watch?v=v0qNmkJSJ8A&t=660s) |

## Projects mentioned

OpenCost, [llm-d](https://github.com/llm-d/llm-d), [vLLM](https://github.com/vllm-project/vllm), [SGLang](https://github.com/sgl-project/sglang), [Prometheus](https://github.com/prometheus/prometheus), [Kubernetes](https://github.com/kubernetes/kubernetes), NVIDIA DCGM, FOCUS
