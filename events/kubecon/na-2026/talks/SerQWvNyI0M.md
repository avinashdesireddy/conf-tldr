# AI Gateways in Practice: Model Routing, Inference Scheduling, and MCP on Kubernetes

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Yuke Ning (Alibaba Cloud)  
**Video:** [YouTube](https://www.youtube.com/watch?v=SerQWvNyI0M) (28:29)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=AI+Gateways+in+Practice%3A+Model+Routing%2C+Inference+Scheduling%2C+and+MCP+on+Kubernetes)  
**Tags:** `ai-inference`, `ai-gateway`, `gateway-api`, `mcp`, `routing`

> Using the Higress gateway, the talk walks through three AI traffic paths on Kubernetes: hosted model providers with fallback, self-hosted models behind Gateway API Inference Extension pools, and agent tool calls over MCP. It compares an endpoint picker embedded in the gateway with an external EPP such as llm-d's, including how each behaves on failure.

## Key points

- Higress, a CNCF sandbox gateway built on Envoy and Istio, puts provider calls, self-hosted inference and MCP tools behind one entry point with shared security, quota and observability, but each path needs a different routing decision. [0:00](https://www.youtube.com/watch?v=SerQWvNyI0M)
- For hosted models, a model router plugin copies the model field from the JSON body to a header for normal route matching; an AI route maps it to weighted providers, and an AI proxy translates protocols, injects API keys and rewrites model names. [3:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=180s)
- Provider fallback lives on the AI route: on 4xx/5xx responses Envoy does an internal redirect to a backup provider and model, and a response header shows that fallback happened. The decision is per request and keeps no state. [5:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=300s)
- API key failover is a separate mechanism inside one provider: a failing key leaves rotation after a threshold and returns after a health check or cooldown, with state kept per gateway pod. [6:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=360s)
- Fallback cannot redirect a streaming response once a 200 has started, 429 and 503 usually need different reactions, and fallback models differ in context window and quality, so map them deliberately. [7:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=420s)
- Self-hosted replicas are not interchangeable: queue depth, KV cache use, prefix cache locality and loaded LoRA adapters matter more than connection counts. An HTTPRoute points at an InferencePool, which references an endpoint picker (EPP). [8:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=480s)
- Higress creates a headless Service per InferencePool and sends request attributes and candidates to the EPP over Envoy external processing; on retries it reports the pod that actually served the response so the picker's view stays accurate. [11:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=660s)
- Embedded option: an AI load balancer Wasm plugin scores pods from per-host metrics (ported from the upstream inference extension scheduler), with Redis for shared state; if it fails, normal service load balancing applies. [13:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=780s)
- External option: an EPP per pool, such as the llm-d inference scheduler, runs filter and scorer plugins and adds prefix-cache-aware routing, prefill/decode disaggregation and latency prediction, at the cost of one more component and a gRPC round trip per request. [15:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=900s)
- Rule of thumb: embedded picker for small pools with simple traffic; external EPP for large pools, when KV cache reuse matters, or when several gateways need the same scheduling. The choice is per route. Fail-close is the default; fail-open favors availability. [18:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=1080s)
- For MCP, the gateway can expose REST APIs as MCP tools via request templates (credentials injected, never seen by the agent), proxy existing MCP servers with auth and rate limits, and bridge clients and servers on different MCP transport versions. [22:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=1320s)

## Numbers stated

- The AI proxy supports 38 provider types. [4:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=240s)
- Higress passes the Gateway API v1.6.0 HTTP profile core tests with no failures or skips; the report was accepted upstream. [21:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=1260s)
- All 12 core tests of the Inference Extension v1.4.0 gateway profile pass; this report is published by the project, not submitted upstream. [21:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=1260s)

## Open gaps

- When every pod is saturated no picker can create capacity; queueing, admission control, gateway rate limits or autoscaling are still needed. [19:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=1140s)
- The Inference Extension conformance report has not been submitted upstream, so it is a project report, not an upstream result. [21:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=1260s)
- MCP's HTTP transport has changed several times in two years, so clients and servers on different versions need bridging. [23:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=1380s)
- The speaker asks for feedback on EPP behavior under real model load and on what breaks during MCP migration. [28:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=1680s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Set up provider fallback with separate rules for 429 and 503, and expose fallback rate in per-route and per-model metrics. | [7:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=420s) |
| learn | Run both an embedded picker and an external EPP on the same gateway and compare them per route, including fail-open versus fail-close. | [18:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=1080s) |
| build | Expose an existing REST API as MCP tools through gateway templates instead of writing a separate MCP server. | [24:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=1440s) |
| contribute | Share EPP behavior data under real load and MCP migration issues with the Higress project. | [28:00](https://www.youtube.com/watch?v=SerQWvNyI0M&t=1680s) |

## Projects mentioned

Higress, Envoy, [Istio](https://github.com/istio/istio), [Gateway API](https://github.com/kubernetes-sigs/gateway-api), [Gateway API Inference Extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension), [llm-d](https://github.com/llm-d/llm-d), [vLLM](https://github.com/vllm-project/vllm), [Redis](https://github.com/redis/redis), Model Context Protocol
