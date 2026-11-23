# Beyond Model Serving: Running Production LLMs on Kubernetes with KServe

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Johnu George (Nutanix), Jooho lee (Red Hat)  
**Video:** [YouTube](https://www.youtube.com/watch?v=WPukEewRCOI) (28:28)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Beyond+Model+Serving%3A+Running+Production+LLMs+on+Kubernetes+with+KServe)  
**Tags:** `ai-inference`, `kserve`, `disaggregated-serving`, `autoscaling`, `routing`

> KServe maintainers explain LLMInferenceService, a separate API from InferenceService that wraps llm-d, vLLM and Gateway API Inference Extension routing so one resource can describe single-node, multi-node and prefill/decode-disaggregated deployments. They then walk through production patterns: cache-aware routing, timeouts, queue-based autoscaling, cold-start reduction, rollouts and LoRA adapters.

## Key points

- LLMs differ from predictive models: they generate tokens over time, hold GPU memory for KV cache, and run long requests, so scheduling, scaling and load balancing need rethinking. [1:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=60s)
- KServe integrates llm-d rather than building an inference engine, and has to keep up with llm-d's fast release pace without bloating its API. [2:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=120s)
- LLMInferenceService has a workload controller (single node, multi-node, separate prefill pool) and a route controller (scheduler and Gateway API resources); it is kept separate so InferenceService stays simple. [4:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=240s)
- One YAML sets model source (Hugging Face, S3, PVC or OCI), tensor/data parallelism, an optional independently scaled prefill pool, and router, gateway and scheduler settings; KServe creates the rest from presets. [7:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=420s)
- The endpoint picker (EPP, the llm-d scheduler) picks a replica using prefix cache match, queue depth and KV cache usage, built on Gateway API Inference Extension; users can plug in a custom EPP. [9:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=540s)
- For streaming, route timeouts must exceed generation time and each hop's timeout must exceed the next one, or clients retry and pile more load on GPUs. [13:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=780s)
- Disaggregated prefill/decode gives consistent TTFT and TPOT at high concurrency and allows different GPU types per phase; very large models use multi-node with LeaderWorkerSet, tensor parallelism within a node and pipeline parallelism across nodes. [14:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=840s)
- Autoscale on the engine's waiting-queue length: GPU utilization reads near 100% with only a few requests because it is a time-share metric, and KV cache utilization sits at a medium baseline. [16:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=960s)
- Cold start: a local model cache, plus container snapshot and restore (CRI-O, NVIDIA Dynamo), cuts startup from tens of minutes to seconds. A shared KV pool keeps TTFT low for new versions during canary rollouts. [17:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=1020s)
- Multiple LoRA adapters on one shared base vLLM model are selected per request and save GPU memory. [20:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=1200s)
- Q&A: KV cache offloading (LMCache, Dynamo, vLLM connectors) is transparent to KServe; the llm-d router must know where blocks are offloaded to route well. [26:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=1560s)

## Numbers stated

- llm-d went from v0.4 in November 2025 to v1.0 the month before the talk. [3:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=180s)
- Pipeline parallelism example: two nodes with eight GPUs each. [15:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=900s)
- Snapshot/restore cuts cold start from tens of minutes to a few seconds. [18:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=1080s)
- Aggregated serving can show P99 at 2-3x baseline versus disaggregated. [24:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=1440s)

## Open gaps

- Next focus is agentic workloads: routing by request type and complexity with llm-d, and SLAs per workload class. [22:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=1320s)
- Fast cold start does not solve rollout traffic: new versions have no KV cache unless a shared KV pool is added. [19:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=1140s)
- Dashboards hide queueing; end-to-end latency can look flat while TTFT and TPOT degrade. [20:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=1200s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Autoscale vLLM replicas in KServe on waiting-queue length instead of GPU utilization. | [17:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=1020s) |
| build | Audit timeouts from client through load balancer, AI gateway and EPP so each exceeds the one downstream. | [21:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=1260s) |
| learn | Start with aggregated LLMInferenceService, then move to prefill/decode disaggregation, then multi-node LeaderWorkerSet as scale grows. | [21:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=1260s) |
| contribute | Help KServe with agentic-workload routing and per-workload SLAs on top of llm-d. | [22:00](https://www.youtube.com/watch?v=WPukEewRCOI&t=1320s) |

## Projects mentioned

[KServe](https://github.com/kserve/kserve), [llm-d](https://github.com/llm-d/llm-d), [vLLM](https://github.com/vllm-project/vllm), [SGLang](https://github.com/sgl-project/sglang), [Gateway API](https://github.com/kubernetes-sigs/gateway-api), [Gateway API Inference Extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension), [LeaderWorkerSet](https://github.com/kubernetes-sigs/lws), [Ray](https://github.com/ray-project/ray), [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo), LMCache, CRI-O, [agentgateway](https://github.com/agentgateway/agentgateway), [Kubernetes](https://github.com/kubernetes/kubernetes)
