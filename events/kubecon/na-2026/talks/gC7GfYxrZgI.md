# From GPU to Fleet. The llm-d KV Cache Hierarchy

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Vita Bortnikov (IBM Research), Nishtha Jain (Google)  
**Video:** [YouTube](https://www.youtube.com/watch?v=gC7GfYxrZgI) (22:16)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=From+GPU+to+Fleet.+The+llm-d+KV+Cache+Hierarchy)  
**Tags:** `ai-inference`, `llm-d`, `vllm`, `kv-cache`, `storage`

> Agent traffic is long input and short output, so reusing KV cache matters more than raw GPU speed. llm-d and vLLM now tier KV cache from GPU to CPU to shared storage and route requests to where the cache already lives.

## Key points

- Agentic workloads read far more than they write; KV cache reuse can reach 95%. [2:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=120s)
- Tiering is upstream: vLLM ships an offloading connector (GPU to CPU to storage, CPU as the core tier) and a storage connector; llm-d owns orchestration and eviction. [4:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=240s)
- Peer-to-peer KV transfer pulls a prefix from a busy pod to a free one, and also powers prefill/decode disaggregation. [6:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=360s)
- Three tiers: GPU HBM (hottest, smallest), CPU DRAM plus local NVMe (about 2 TB), and shared network storage such as Lustre or IBM Storage Scale. [11:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=660s)
- Plain NFS volumes do not scale for this; parallel file systems give the throughput needed. [13:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=780s)
- Storage offloading without storage-aware routing fails at scale: requests land on pods that do not hold the cache. [19:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=1140s)
- Setup: an RWX PVC, pinned CPU memory and the offloading connector on vLLM (SGLang also supported), plus KV events and endpoint-picker config in the llm-d router. [20:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=1200s)

## Numbers stated

- An 80 GB GPU leaves about 15 GB for KV cache after model weights and buffers. [9:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=540s)
- Over 50% TCO savings and about 60% fewer GPU hours with external storage attached. [14:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=840s)
- About 40% better time to first token and 30% more QPS with the hybrid setup. [15:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=900s)
- Llama 70B at 128k tokens: reading KV from network storage is about 10x faster than recomputing. [16:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=960s)
- Speedup over recompute: HBM about 40x, DRAM about 21x, network storage about 10x. [17:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=1020s)
- Replayed Claude Code traces, 50 to 800 users: GPU-only saturates past 100 users; GPU+CPU hits a cliff near 300; GPU+CPU+storage stays flat above 2,500 output tok/s up to 800 users. [18:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=1080s)
- Turning off the storage index in the router dropped throughput from about 2,500 to 700 tok/s at 800 users. [19:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=1140s)
- About 1.2 billion KV tokens written to storage in the run. [19:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=1140s)

## Open gaps

- Writing a new KV connector in vLLM used to be very hard; the new offloading connector is meant to make it pluggable, and more connectors are wanted. [5:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=300s)
- KV footprint keeps growing with context length (up to a million tokens), so capacity planning across tiers is an ongoing problem. [9:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=540s)
- The speakers ask for more contributions to the guides and to the KV Cache SIG. [22:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=1320s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Reproduce the GPU-only vs GPU+CPU vs GPU+CPU+storage curve on a managed Kubernetes service with a shared file system (for example FSx for Lustre) and publish the guide. | [18:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=1080s) |
| contribute | Add a storage backend to the vLLM offloading connector or an llm-d well-lit-path guide for another cloud's parallel file system. | [20:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=1200s) |
| write | Explain 'storage offloading needs storage-aware routing' with the 2,500 vs 700 tok/s result as the hook. | [19:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=1140s) |
| learn | Join the llm-d KV Cache SIG to follow tiering and P2P work. | [22:00](https://www.youtube.com/watch?v=gC7GfYxrZgI&t=1320s) |

## Projects mentioned

[llm-d](https://github.com/llm-d/llm-d), [vLLM](https://github.com/vllm-project/vllm), [SGLang](https://github.com/sgl-project/sglang), [Lustre](https://www.lustre.org/), IBM Storage Scale, [NIXL](https://github.com/ai-dynamo/nixl), [Mooncake](https://github.com/kvcache-ai/Mooncake), [Prometheus](https://github.com/prometheus/prometheus)
