# Inside the Inference Load Balancer: Proxy/Controller Patterns for LLM Serving on Kubernetes

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Qianru Lao (OpenAI), Lu Zhang (OpenAI)  
**Video:** [YouTube](https://www.youtube.com/watch?v=wNJVJ8PhFO0) (31:19)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Inside+the+Inference+Load+Balancer%3A+Proxy%2FController+Patterns+for+LLM+Serving+on+Kubernetes)  
**Tags:** `ai-inference`, `routing`, `multi-cluster`, `load-balancing`, `production`

> OpenAI's inference load balancer picks a GPU engine for every request across clusters and regions. A global control plane computes routing weights from demand, capacity and latency profiles; fast local data planes apply them, with penalties, retry caps and load shedding for protection.

## Key points

- The load balancer runs in CPU front-end clusters and proxies requests to inference engines in GPU clusters; both sides run on Kubernetes. [2:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=120s)
- The least-busy engine is not always fastest: one that already caches the conversation reaches the first token sooner. Signals are TTFT, time between output tokens, load, errors, network latency and cache affinity. [4:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=240s)
- The balancer itself is plain Kubernetes: Deployments, HPA on CPU and custom metrics, readiness probes, and GPU cluster locations from a ConfigMap. [5:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=300s)
- Early design: filter eligible engines (capabilities, data location), then weighted consistent hashing, with weights nudged by a proportional feedback loop. [6:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=360s)
- That design was hard to explain, unbalanced across GPU generations, and weight shifts broke cache affinity, causing oscillation. [9:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=540s)
- Current design copies Kubernetes' control/data plane split (like kube-proxy and EndpointSlices): each data plane routes from locally cached weights, never calling the control plane per request. [12:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=720s)
- Nearest-engine routing fails because demand and GPU capacity are not balanced by region; a farther engine can win end to end. [17:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=1020s)
- The optimizer takes per-cluster demand, network latency, engine capacity and health, and latency-vs-load profiles, and minimizes expected end-to-end latency subject to capacity limits. [18:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=1080s)
- Protection: outlier penalties, bounded retries (retries are costly because the new engine lacks the cache), and load shedding as a last resort. [21:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=1260s)
- Q&A: spiky API traffic uses other algorithms, more headroom and wider destination pools; uncached tokens are the work measure; each model version is routed as its own model. [26:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=1560s)

## Numbers stated

- Optimized routing weights cut network overhead by about 40%. [20:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=1200s)
- Example: a cluster sending 120 RPS to a 100 RPS engine nearby, while another region uses only 40 of 80 RPS. [17:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=1020s)

## Open gaps

- Bursty API traffic against lagging state can still overload a few engines. [25:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=1500s)
- Retry caps that suit normal load can be too high during fleet-wide overload. [22:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=1320s)
- Persistent engine faults still need manual investigation and vendor follow-up. [21:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=1260s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| write | Compare this control/data plane design with llm-d's endpoint picker and Gateway API inference routing. | [12:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=720s) |
| build | Prototype a global routing-weight optimizer for multi-region inference, with latency-vs-load profiles per engine. | [18:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=1080s) |
| build | Add cache-aware retry budgets and load shedding to your inference gateway. | [22:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=1320s) |
| learn | Proportional and PID control, and why mixing many signals into one weight oscillates. | [7:00](https://www.youtube.com/watch?v=wNJVJ8PhFO0&t=420s) |

## Projects mentioned

[Kubernetes](https://github.com/kubernetes/kubernetes)
