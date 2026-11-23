# New Traffic, New Rules: Standardizing AI-Aware Networking in Kubernetes

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Nir Rozenbaum (NVIDIA), Keith Mattix (Solo.io)  
**Video:** [YouTube](https://www.youtube.com/watch?v=kwJTUGK4FPM) (31:48)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=New+Traffic%2C+New+Rules%3A+Standardizing+AI-Aware+Networking+in+Kubernetes)  
**Tags:** `ai-inference`, `gateway-api`, `networking`, `standards`, `routing`

> The Kubernetes AI Gateway Working Group presents its proposals for AI-aware traffic in Gateway API: pre-routing payload processing, a Backend resource, an endpoint selector, gateway routability and multi-stage routes. The goal is one standard set of APIs so different routers stop building their own body parsing, egress and inference orchestration.

## Key points

- The working group started about a year ago to standardize AI-aware traffic management at the gateway layer, reusing Gateway API building blocks and adding primitives only where they are missing. [1:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=60s)
- Gateway API routes on headers, path and query, but AI signals such as the model name live in the request body. Today everyone solves this with ext_proc, Lua or Wasm, none of it standard. [3:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=180s)
- Pre-routing filters, already in experimental, run an ordered list of filters before route selection. Paired with a filter that promotes a body field to a header, this enables body-based routing in process; external processing is future work. [4:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=240s)
- Service does two jobs: a producer-owned front end (stable DNS name, cluster IP) and a consumer-oriented back end (endpoints, ports, protocol). Service is effectively frozen, so new features are hard to add there. [8:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=480s)
- AI apps call external model APIs constantly, and ExternalName services are seen as unsafe and often banned. The new Backend resource, now experimental in Gateway API, covers in-cluster endpoint selectors or external hostnames plus TLS and protocol settings. [11:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=660s)
- Backend does not replace Service; it is a fit-for-purpose place to add things like session persistence, TLS and later MCP. [13:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=780s)
- Inference routers such as the llm-d endpoint picker need a bag of endpoints without a cluster IP, because clients using the Service VIP or DNS name bypass the picker and lose KV cache hits. The endpoint selector proposal to upstream Kubernetes reuses label-selector machinery for this. [15:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=900s)
- The routability proposal lets a Gateway declare how its address is reachable (for example cluster-only), which matters for egress gateways that would otherwise become open relays. It is not access control; that remains NetworkPolicy. [19:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=1140s)
- Distributed inference no longer maps one request to one endpoint: a request may pass tokenization, guardrails, then encode, prefill and decode. Multi-stage routes reference existing HTTPRoutes and control stage order and skip conditions, reusing their retries and backoff. [22:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=1320s)
- Payload processing defines what happens between stages, such as passing prefill output as metadata to the decode request; the scheduling intelligence stays in the application layer. [26:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=1560s)
- Q&A: keep using Service for normal workloads; Backend is for specialized cases, AI or complex mesh setups, where endpoints need extra metadata. [29:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=1740s)

## Open gaps

- External processing for payload handling is not yet supported; only in-process filters are in scope so far. [7:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=420s)
- Multi-stage route syntax is illustrative and not finalized, and the between-stage data passing still has to be defined. [26:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=1560s)
- Next proposals include token-based rate limiting, plus consolidating the separate AI networking efforts in SIG Network into one community. [28:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=1680s)
- Routability cannot control what the cloud provider network exposes, so cluster scope is not a security guarantee. [21:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=1260s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| contribute | Join the AI Gateway Working Group calls and help move payload processing, Backend and multi-stage routes toward GA. | [28:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=1680s) |
| build | Prototype body-based model routing using pre-routing filters that promote the model field to a header. | [6:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=360s) |
| learn | Read the Kubernetes blog post on the Backend resource and compare it to how your gateway handles external model egress and TLS today. | [13:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=780s) |
| write | Map how existing distributed inference projects orchestrate tokenize, prefill and decode stages, as input to the multi-stage route design. | [24:00](https://www.youtube.com/watch?v=kwJTUGK4FPM&t=1440s) |

## Projects mentioned

[Gateway API](https://github.com/kubernetes-sigs/gateway-api), [Gateway API Inference Extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension), [llm-d](https://github.com/llm-d/llm-d), [Kubernetes](https://github.com/kubernetes/kubernetes), [vLLM](https://github.com/vllm-project/vllm), [Istio](https://github.com/istio/istio), Linkerd, Cilium, Knative
