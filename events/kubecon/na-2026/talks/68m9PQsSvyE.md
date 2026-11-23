# Seeing Inside LLM Inference: Observability and Cost Visibility for llm-d on Kubernetes

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Nili Guy (IBM), Guangya Liu (JPMorgan Chase)  
**Video:** [YouTube](https://www.youtube.com/watch?v=68m9PQsSvyE) (15:35)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Seeing+Inside+LLM+Inference%3A+Observability+and+Cost+Visibility+for+llm-d+on+Kubernetes)  
**Tags:** `ai-inference`, `observability`, `tracing`, `cost`, `llm-d`

> The llm-d observability and router SIG leads show end-to-end tracing of a request through the gateway, endpoint picker, KV cache lookup and prefill/decode pods, and use metric-to-trace-to-log correlation to find a bad scorer weight behind a TTFT regression. They then describe combining llm-d metrics with OpenCost to compute per-token, per-tenant cost, which is early work that is already upstream.

## Key points

- A request flows from Envoy to the endpoint picker (EPP), which checks KV cache state, picks prefill and decode pods, and a sidecar sends the prompt to prefill, after which decode pulls the KV cache GPU to GPU. [1:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=60s)
- One trace covers tokenization, longest-prefix cache lookup, profile and scorer runs, endpoint selection, and prefill/decode; routing is a tiny part of the timeline. [2:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=120s)
- Span attributes include the longest cached prefix in blocks, top endpoints and scores, TTFT and queue latency. [3:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=180s)
- Grafana links metrics to traces in Jaeger with one click; logs carry trace and span IDs, but log-trace correlation is not in the dashboard yet, so you grep the trace ID. [4:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=240s)
- Demo: a P99 TTFT alert led to a trace where the pod without the cache won because the cache scorer weight was zero, so the prompt was recomputed. [5:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=300s)
- No error logs appeared; the EPP behaved correctly on a bad config, traced to a Helm release that changed the weight from 3 to 0. [6:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=360s)
- Cost has two views: allocation (deployed capacity on given hardware) and usage (per-tenant, per-user tokens), with cost per token as total cost over tokens served. [10:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=600s)
- llm-d router and gateway metrics plus vLLM or SGLang metrics go to Prometheus; OpenCost combines them with infrastructure cost and emits cost metrics at different granularities. [13:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=780s)
- The goal is to compare self-hosted open-weights serving with sending requests to external providers, and to spot idle GPUs. [10:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=600s)
- Dashboards, observability and the OpenCost integration are all upstream in llm-d. [15:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=900s)

## Numbers stated

- Alert fired on P99 TTFT above 250 ms for more than 2 minutes; P99 jumped from about 200 ms to 600 ms. [4:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=240s)
- Scores: cached pod 3.86 versus uncached pod 3.93 once the cache weight was zero. [5:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=300s)
- Prefill took about 569 ms for about 4,000 tokens, 10x a healthy prefill. [6:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=360s)
- Good vs bad trace for a ~3,800-token, fully cached prompt (59 blocks): 152 ms prefill with weight 3, 569 ms with weight 0. [7:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=420s)

## Open gaps

- Log-to-trace correlation is not supported from the dashboard yet; it relies on grepping trace IDs. [4:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=240s)
- The OpenCost cost model for llm-d is initial work, still being evaluated in production. [14:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=840s)
- Per-tenant and per-user cost granularity across shared models on mixed hardware is still being worked out. [11:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=660s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| learn | Use EPP trace attributes (prefix blocks, scores, chosen endpoint) to debug routing regressions. | [3:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=180s) |
| build | Add alerts on scorer config changes, since a bad weight produced no error logs. | [7:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=420s) |
| contribute | Add log-trace correlation to the upstream llm-d Grafana dashboards. | [4:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=240s) |
| build | Feed llm-d and vLLM metrics into OpenCost to compare self-hosted cost per token with external API pricing. | [14:00](https://www.youtube.com/watch?v=68m9PQsSvyE&t=840s) |

## Projects mentioned

[llm-d](https://github.com/llm-d/llm-d), [vLLM](https://github.com/vllm-project/vllm), [SGLang](https://github.com/sgl-project/sglang), Envoy, [Prometheus](https://github.com/prometheus/prometheus), Grafana, [Jaeger](https://github.com/jaegertracing/jaeger), OpenCost, Helm
