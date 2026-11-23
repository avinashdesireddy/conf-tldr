# Agentic Inference at Scale

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Maroon Ayoub (Red Hat), Sean Horgan (Google)  
**Video:** [YouTube](https://www.youtube.com/watch?v=7gvpGm3GCB4) (19:12)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Agentic+Inference+at+Scale)  
**Tags:** `ai-inference`, `llm-d`, `agents`, `day-2-operations`, `multi-tenancy`

> Agent sessions send about 100 tokens in for every token out, so serving them well is about never recomputing context. llm-d 1.0 packages cache-aware routing, offloading and disaggregation, adds day-2 operations, and a new SIG is moving scheduling from single requests to whole sessions.

## Key points

- Agent sessions have roughly a 100:1 input to output ratio, so the reuse ceiling is close to 100%. [0:00](https://www.youtube.com/watch?v=7gvpGm3GCB4)
- Watch prefill compute as a metric: a hidden cache-buster can sit behind a healthy-looking hit rate. [3:00](https://www.youtube.com/watch?v=7gvpGm3GCB4&t=180s)
- The llm-d router balances prefix-cache affinity against load-aware routing so stickiness does not create hot spots. [6:00](https://www.youtube.com/watch?v=7gvpGm3GCB4&t=360s)
- Keep idle sessions alive: north-south offload to CPU and storage, east-west P2P pull when a session moves pods. [7:00](https://www.youtube.com/watch?v=7gvpGm3GCB4&t=420s)
- Prefill/decode disaggregation also isolates failures: a cache-hit collapse in an aggregated deployment hurts decode users too. [8:00](https://www.youtube.com/watch?v=7gvpGm3GCB4&t=480s)
- llm-d 1.0 focus is day-2: a new router loads a state snapshot, warms instantly, and takes traffic with zero errors. [10:00](https://www.youtube.com/watch?v=7gvpGm3GCB4&t=600s)
- Flow control queues batch tenants so interactive TTFT stays flat while total throughput is maximized. [12:00](https://www.youtube.com/watch?v=7gvpGm3GCB4&t=720s)
- The Agentic Inference SIG is designing session-level orchestration: a KV block index, session state (compaction, forks, sub-agents), a KV hints envelope (pin, copy, move) and session-aware admission instead of FIFO. [14:00](https://www.youtube.com/watch?v=7gvpGm3GCB4&t=840s)

## Numbers stated

- Published Weka traces show 95% achieved prefix reuse. [1:00](https://www.youtube.com/watch?v=7gvpGm3GCB4&t=60s)
- Production: prefill compute was 16% at an 85% hit rate; after fixing a per-turn timestamp Claude Code injects into the system prompt, prefill dropped to 4% while traffic doubled. [3:00](https://www.youtube.com/watch?v=7gvpGm3GCB4&t=180s)
- A 6-hour non-interactive ramp was queued with no visible change to interactive TTFT. [12:00](https://www.youtube.com/watch?v=7gvpGm3GCB4&t=720s)

## Open gaps

- Routers see requests, not sessions: an agent paused on a tool call looks idle, gets evicted, and pays full recompute on return. [17:00](https://www.youtube.com/watch?v=7gvpGm3GCB4&t=1020s)
- Agent harnesses do not yet emit rich session state; the SIG wants to co-design that signal with client projects. [15:00](https://www.youtube.com/watch?v=7gvpGm3GCB4&t=900s)
- Closed-source agent clients can break cache reuse in open serving stacks (the timestamp-in-system-prompt bug). [3:00](https://www.youtube.com/watch?v=7gvpGm3GCB4&t=180s)
- Explainability: operators cannot yet tell whether their hit rate is the hardware ceiling or a bug. [7:00](https://www.youtube.com/watch?v=7gvpGm3GCB4&t=420s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Add a prefill-compute-percent panel to an inference dashboard and alert on it, not just on hit rate. | [3:00](https://www.youtube.com/watch?v=7gvpGm3GCB4&t=180s) |
| contribute | Help the Agentic Inference SIG define the session-state signal an agent harness should send to the router. | [15:00](https://www.youtube.com/watch?v=7gvpGm3GCB4&t=900s) |
| write | Case study: how one system-prompt timestamp cut cache reuse, and how to find that kind of bug. | [3:00](https://www.youtube.com/watch?v=7gvpGm3GCB4&t=180s) |
| build | Demo flow control with batch plus interactive tenants on one cluster, showing flat interactive TTFT. | [12:00](https://www.youtube.com/watch?v=7gvpGm3GCB4&t=720s) |

## Projects mentioned

[llm-d](https://github.com/llm-d/llm-d), [vLLM](https://github.com/vllm-project/vllm), [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo), [SGLang](https://github.com/sgl-project/sglang), [Mooncake](https://github.com/kvcache-ai/Mooncake), Claude Code
