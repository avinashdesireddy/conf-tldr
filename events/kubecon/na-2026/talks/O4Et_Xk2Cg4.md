# llm-d 1.0 Production-Grade Inference for Cloud-Native AI

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Carlos Costa (IBM Research), Robert Shaw  
**Video:** [YouTube](https://www.youtube.com/watch?v=O4Et_Xk2Cg4) (21:17)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=llm-d+1.0+Production-Grade+Inference+for+Cloud-Native+AI)  
**Tags:** `ai-inference`, `llm-d`, `flow-control`, `multi-tenancy`, `open-weights`

> llm-d 1.0 marks the core stack as production-ready: KV-aware routing, prefill/decode disaggregation, KV offloading and flow control, behind a stable v1 API. IBM ran it on 500+ H100s for an internal agentic workload, and a demo shows throughput nearly doubling on the same hardware.

## Key points

- Open-weight models now close much of the gap with frontier models, so enterprises want to self-host for cost and data control. [0:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4)
- Scaling inference is an orchestration problem: route on KV reuse and load, schedule multi-pod replicas as gangs, and manage KV state across memory tiers. [1:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=60s)
- llm-d builds on Kubernetes standards: the Gateway API inference extension for the router, LeaderWorkerSet for MoE and gang scheduling, DisaggregatedSet for prefill/decode, and native KV offloading. [3:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=180s)
- It now also supports batch and async APIs. [4:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=240s)
- Design stays modular (use only what you need) and vendor-neutral, with more than eight accelerator types supported. [5:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=300s)
- 'Well-lit paths' are deployable blueprints with benchmark data: intelligent scheduling, KV cache management, flow control, and now agentic serving. [6:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=360s)
- 1.0 adds multi-tenant QoS (priority and fairness via flow control), router high availability, coordinated prefill/decode rollouts, session and turn affinity for agents, and a stable v1 API. [14:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=840s)
- Demo: with plain round robin the KV cache hit rate is low and uneven; turning on the llm-d router raises it to about 75% and nearly doubles throughput; flow control then gives paying tiers lower latency while free users still get served. [17:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=1020s)

## Numbers stated

- A new open-weight model drops about every 11 days. [0:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4)
- Tesla saw 3x more throughput with KV-aware routing. [8:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=480s)
- Over 500 contributors and more than 25 contributing companies. [8:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=480s)
- IBM: 500+ H100 GPUs serving a large MoE model with expert parallelism of 32+, peaking at 3,000 concurrent agents and about 6 million tokens a minute (6x what the workload needed). [10:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=600s)
- Demo: 1,000 agents on 25 Kubernetes nodes across 40 sandboxes, about 300 requests a second. [16:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=960s)
- KV cache hit rate rose from a 30-50% swing to about 75% with the llm-d router. [18:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=1080s)

## Open gaps

- Going from a model recipe to a shared service (rollouts, downtime, competing teams) is still the hard part. [1:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=60s)
- Tuning still takes a lot of expertise; the roadmap names operational intelligence, more automation and better guides. [20:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=1200s)
- Agent infrastructure (sandboxes, agent-substrate) and inference infrastructure are not yet woven together for fully self-hosted stacks. [19:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=1140s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Reproduce the round robin vs llm-d router vs flow control comparison on your own cluster and publish the numbers. | [17:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=1020s) |
| contribute | Run a well-lit path on hardware or a model it has not been tested on and report how it breaks, as the speakers ask. | [20:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=1200s) |
| write | Case study: serving a large MoE model on previous-generation GPUs instead of paying a commercial API bill. | [10:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=600s) |
| learn | Read through llm-d's well-lit paths as the shortest route to a tuned deployment. | [6:00](https://www.youtube.com/watch?v=O4Et_Xk2Cg4&t=360s) |

## Projects mentioned

[llm-d](https://github.com/llm-d/llm-d), [vLLM](https://github.com/vllm-project/vllm), [SGLang](https://github.com/sgl-project/sglang), [Gateway API Inference Extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension), [LeaderWorkerSet](https://github.com/kubernetes-sigs/lws), [Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox)
