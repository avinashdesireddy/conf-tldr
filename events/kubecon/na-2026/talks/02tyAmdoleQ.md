# Composing Inference on Kubernetes: Gateway, Schedule, Serve, Observe

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Karena Angell (Red Hat), Alex Chircop (Google)  
**Video:** [YouTube](https://www.youtube.com/watch?v=02tyAmdoleQ) (30:03)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Composing+Inference+on+Kubernetes%3A+Gateway%2C+Schedule%2C+Serve%2C+Observe)  
**Tags:** `ai-inference`, `platform-engineering`, `gateway-api`, `observability`, `composability`

> Production inference should be built from open, swappable layers: accelerators, scheduling, gateway, serving and observability. The test is whether you can swap one layer, such as vLLM for SGLang or one endpoint picker for another, without the others noticing.

## Key points

- Inference is too often a closed vertical: one gateway, one serving image, one observability silo. [0:00](https://www.youtube.com/watch?v=02tyAmdoleQ)
- Composability has six lenses: workload, control flow, resource, information, human-agent and architectural. [1:00](https://www.youtube.com/watch?v=02tyAmdoleQ&t=60s)
- Workloads nest (a model call inside RAG inside an agent inside a business workflow); separate platforms per type duplicate routing, scheduling and telemetry. [2:00](https://www.youtube.com/watch?v=02tyAmdoleQ&t=120s)
- On shared clusters the model endpoint becomes everyone's dependency with no isolation or back pressure, and nobody can tell where tail latency was spent. [3:00](https://www.youtube.com/watch?v=02tyAmdoleQ&t=180s)
- Layer model: Kubernetes control plane, accelerators via DRA, then gateway, scheduler and serving, all wrapped in observability. [4:00](https://www.youtube.com/watch?v=02tyAmdoleQ&t=240s)
- A fixed DAG gives predictable latency and token spend; autonomous agents trade that for flexibility. [7:00](https://www.youtube.com/watch?v=02tyAmdoleQ&t=420s)
- Admission (Kueue, Volcano, KAI Scheduler) decides whether pods can exist; the endpoint picker decides which replica serves this prompt now. They are different jobs. [14:00](https://www.youtube.com/watch?v=02tyAmdoleQ&t=840s)
- Because the picker sits behind the Gateway API, pickers and gateways (llm-d, the GIE reference picker, Envoy Gateway, agentgateway, kgateway, Istio) can be swapped without client changes. [15:00](https://www.youtube.com/watch?v=02tyAmdoleQ&t=900s)
- Carry knowledge, context, state and provenance across hops with OpenTelemetry GenAI semantic conventions and W3C traceparent; Kepler adds GPU energy. [16:00](https://www.youtube.com/watch?v=02tyAmdoleQ&t=960s)
- Serving boundary test: when TGI went into maintenance, teams behind a clean gateway contract swapped engines quickly. If swapping vLLM for SGLang breaks routing, auth or dashboards, the serving layer is doing platform work. [18:00](https://www.youtube.com/watch?v=02tyAmdoleQ&t=1080s)
- Agents need security isolation, durable state and fast suspend/resume; agent-substrate, OpenShell and gVisor each cover part of that. [20:00](https://www.youtube.com/watch?v=02tyAmdoleQ&t=1200s)

## Numbers stated

- Lab demo: five traffic shapes (warm-cache chat, agent tool bursts, multi-tenant traffic, queued batch) on one cluster without re-platforming. [10:00](https://www.youtube.com/watch?v=02tyAmdoleQ&t=600s)

## Open gaps

- Teams disagree on what words like 'cached' or 'completed' mean, so traces line up syntactically but not semantically. [17:00](https://www.youtube.com/watch?v=02tyAmdoleQ&t=1020s)
- Idle agent pods waiting on the model or a human waste cluster memory and risk losing state. [21:00](https://www.youtube.com/watch?v=02tyAmdoleQ&t=1260s)
- Autonomous control flow makes spend and termination hard to predict. [7:00](https://www.youtube.com/watch?v=02tyAmdoleQ&t=420s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Run the swap test on your platform: change the serving engine and check that routing, auth and dashboards survive. | [19:00](https://www.youtube.com/watch?v=02tyAmdoleQ&t=1140s) |
| build | Propagate W3C traceparent with OpenTelemetry GenAI spans from gateway to picker to model for per-request cost attribution. | [17:00](https://www.youtube.com/watch?v=02tyAmdoleQ&t=1020s) |
| write | Turn the talk's 'diagnose by boundary' checklist into a troubleshooting guide. | [23:00](https://www.youtube.com/watch?v=02tyAmdoleQ&t=1380s) |
| learn | Learn where Kueue-style admission ends and endpoint-picker routing begins. | [14:00](https://www.youtube.com/watch?v=02tyAmdoleQ&t=840s) |

## Projects mentioned

[Kubernetes](https://github.com/kubernetes/kubernetes), [llm-d](https://github.com/llm-d/llm-d), [Gateway API](https://github.com/kubernetes-sigs/gateway-api), [Gateway API Inference Extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension), [Kueue](https://github.com/kubernetes-sigs/kueue), [Volcano](https://github.com/volcano-sh/volcano), [KAI Scheduler](https://github.com/kai-scheduler/KAI-Scheduler), [HAMi](https://github.com/Project-HAMi/HAMi), [KubeRay](https://github.com/ray-project/kuberay), [KEDA](https://github.com/kedacore/keda), [KServe](https://github.com/kserve/kserve), [vLLM](https://github.com/vllm-project/vllm), [SGLang](https://github.com/sgl-project/sglang), [Triton Inference Server](https://github.com/triton-inference-server/server), [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-collector), [Prometheus](https://github.com/prometheus/prometheus), [Kepler](https://github.com/sustainable-computing-io/kepler), [gVisor](https://github.com/gvisor/gvisor), [agentgateway](https://github.com/agentgateway/agentgateway), [kgateway](https://github.com/kgateway-dev/kgateway), [Istio](https://github.com/istio/istio), [Jaeger](https://github.com/jaegertracing/jaeger)
