# Choose Your Own Adventure: The Saga of Serving LLM Inference

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Whitney Lee (Datadog), Viktor Farcic (Upbound)  
**Video:** [YouTube](https://www.youtube.com/watch?v=gNAANhDs5cc) (30:50)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Choose+Your+Own+Adventure%3A+The+Saga+of+Serving+LLM+Inference)  
**Tags:** `ai-inference`, `quantization`, `speculative-decoding`, `tensor-parallelism`, `benchmarking`

> The audience voted on three vLLM serving choices (quantization, sharding versus replication, speculative decoding) and the speakers deployed that configuration and its opposite side by side under load. The audience's full-precision, sharded, speculative setup was more accurate but served fewer requests, and the speakers' advice is to run experiments, not pick in advance.

## Key points

- The audience chose full precision, one model sharded across two GPUs, and n-gram speculative decoding; a second deployment used the opposite choices. [1:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=60s)
- A model scores every possible next token (about 150,000 for the demo model) and the inference engine picks one; knowledge is spread across all weights, so almost all weights are read for every token. [5:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=300s)
- Weights and KV cache compete for GPU memory; quantization stores each weight with fewer bits, freeing room for more and longer conversations and reducing memory reads, at the cost of drifting from how the model was trained. [9:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=540s)
- Switching to the quantized variant was just a different model image (Qwen3 8B to its FP8 version); not every model can go to 4 bits. [15:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=900s)
- Replication gives independent engines, KV caches and no GPU-to-GPU traffic but needs a model small enough and sticky routing; sharding splits weights and KV cache and needs fast GPU interconnect. [16:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=960s)
- Replication tends to win with many concurrent requests and enough KV cache; sharding tends to win with few requests, fast links, or models too big for one GPU. [19:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=1140s)
- Sharding was configured as one copy on two GPUs plus tensor parallel size 2 passed to vLLM. [20:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=1200s)
- Prefill processes known tokens in parallel and is compute-bound; decode is sequential and memory-bandwidth-bound. [22:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=1320s)
- Speculative decoding drafts several tokens (here n-gram, deterministic pattern matching on the conversation) and the model verifies them in one pass, trading compute for memory bandwidth; it is less useful when the GPU is already at high load. [24:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=1440s)
- Advice: you cannot make these choices in advance; serve variants in parallel with round-robin routing and compare. The demo sent telemetry via OpenTelemetry to Datadog. [28:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=1680s)

## Numbers stated

- Demo model: Qwen3 8B, 8 billion parameters, 16-bit weights by default. [7:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=420s)
- Each demo GPU has 24 GB of memory; at full precision about 3 GB per GPU is left for conversations. [12:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=720s)
- Quantized, about 9 GB would hold weights and 9.6 GB would be free for conversations. [13:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=780s)
- The audience's configuration served 30-40% fewer requests and processed fewer tokens per second. [27:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=1620s)
- The audience's full-precision configuration answered the math test prompts 100% correctly. [27:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=1620s)
- Speculative decoding drafted up to four tokens ahead. [26:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=1560s)

## Open gaps

- Whether quantization hurts answers for your use case has to be measured with your own experiments. [11:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=660s)
- Many requests failed on the audience's configuration for reasons the speakers did not have time to explore. [27:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=1620s)
- Some models have no prebuilt quantized image, which makes quantizing painful. [15:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=900s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Deploy two vLLM configurations side by side with round-robin routing and compare throughput and accuracy on your own prompts. | [29:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=1740s) |
| learn | Prefill versus decode bottlenecks (compute versus memory bandwidth) and how speculative decoding trades one for the other. | [22:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=1320s) |
| build | Add a small accuracy check (for example known math prompts) to load tests when evaluating quantized models. | [27:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=1620s) |
| write | Benchmark replication versus tensor-parallel sharding on your GPU interconnect at different concurrency levels. | [19:00](https://www.youtube.com/watch?v=gNAANhDs5cc&t=1140s) |

## Projects mentioned

[vLLM](https://github.com/vllm-project/vllm), [Kubernetes](https://github.com/kubernetes/kubernetes), [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-collector), Datadog, Model Plane
