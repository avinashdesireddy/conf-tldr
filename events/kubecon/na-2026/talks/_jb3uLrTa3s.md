# Dropping LLM Inference Cost by Two-Thirds with Open Weights and Kubernetes

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Omisha Gupta (AWS)  
**Video:** [YouTube](https://www.youtube.com/watch?v=_jb3uLrTa3s) (27:06)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Dropping+LLM+Inference+Cost+by+Two-Thirds+with+Open+Weights+and+Kubernetes)  
**Tags:** `ai-inference`, `fine-tuning`, `cost`, `autoscaling`, `quantization`

> An AWS solutions architect replaced a proprietary LLM API in a multi-label classification pipeline with a QLoRA-fine-tuned Qwen3 8B model served by vLLM on EKS, raising exact-match accuracy from 56% to 91% at one-third of the cost. Quantization, prefix caching and speculative decoding raised per-GPU throughput, but surges exposed slow GPU capacity, which was fixed with smaller and pre-baked images and headroom.

## Key points

- Proprietary APIs cost scales one-to-one with traffic, you pay for intelligence a narrow task does not need, and model upgrades can break tuned prompts: one newer model broke the required JSON format. [1:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=60s)
- The task is a single bounded call (pick every label that applies to a piece of feedback), so it needs a reliable specialist model, not an agent that plans. [5:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=300s)
- Fine-tune when the task is narrow and repeats, you have labeled data, volume makes cost matter, prompting has plateaued and output must be predictable; stay on prompts when the task changes weekly, volume is low, reasoning is open-ended or there is no labeled data. [7:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=420s)
- QLoRA with Unsloth trains a small adapter on a frozen 4-bit base; the adapter was then merged into the base, since there is only one task, instead of hot-swapping adapters with vLLM multi-LoRA. [9:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=540s)
- Training recipe: JSON-formatted labeled data, rare multi-label records repeated three times to balance, rank 32 adapter, evaluation on a held-out unseen set. [10:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=600s)
- The whole pipeline runs as Kubernetes Jobs on the serving cluster: CPU-only data prep, a GPU training job on a Karpenter pool capped as a spend guardrail, merge and AWQ quantization, and a vLLM eval that gates deployment on accuracy. [12:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=720s)
- AWQ 4-bit quantization barely moved accuracy; the real payoff was freeing GPU memory for KV cache on a single A10G instance. [15:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=900s)
- vLLM continuous batching, prefix caching and speculative decoding (answer IDs are copied from the prompt, so guesses are often right) added throughput without more GPUs. [16:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=960s)
- Stack: EKS, Karpenter for GPU nodes, NVIDIA device plugin, one vLLM pod per GPU node, and Prometheus plus KEDA scaling on vLLM running and waiting requests; scale up fast, scale down slowly. [17:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=1020s)
- In a surge test the autoscaler asked for the right replicas but GPU capacity arrived late, so most requests timed out. [20:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=1200s)
- Fixes: zstd-compressed image on a fast disk, image and model pre-baked into the node image, headroom kept for bursts, and GPU capacity spread across regions. [22:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=1320s)

## Numbers stated

- One newer model broke the JSON output format 18% of the time. [1:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=60s)
- Average prompt size grew from 1.5K to over 6K tokens in a year (OpenRouter study cited). [2:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=120s)
- Exact-match accuracy: 56% for the best prompted general API, 12% for Qwen3 8B out of the box, 91% after fine-tuning. [6:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=360s)
- About 10,000 labeled examples; adapter about 1% of the model (334 MB), trained on one GPU in about 12 hours. [8:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=480s)
- Model shrank from 16 GB to 5.7 GB with 4-bit AWQ; KV cache capacity grew 3.6x from 27K tokens. [14:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=840s)
- Serving on a G5 xlarge (A10G, 24 GB) at about $1 per hour on demand: 5.7 GB model, 12 GB KV cache. [15:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=900s)
- 42% more requests per GPU overall; P95 latency from 8.5 to 6.3; speculative decoding guesses accepted 62% of the time. [16:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=960s)
- KEDA scales on in-flight requests divided by 16; Prometheus scrapes vLLM every 5 seconds; model load about 2 minutes. [18:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=1080s)
- Surge test: traffic rose 8x, queue climbed to 2,800 requests, KEDA asked for 10 replicas but got 1, and only 18% of requests were served. [20:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=1200s)
- Container image cut from 11 GB to 7.3 GB; image pull from 5 minutes to 1 minute; a new GPU node useful in about 4 minutes; 5% headroom kept. [22:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=1320s)
- Cost fell to 33% of the API baseline while accuracy rose from 56% to 91%. [23:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=1380s)

## Open gaps

- Autoscalers react correctly but GPU capacity arrives too late for minute-scale surges. [21:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=1260s)
- GPU shortages mean capacity has to be spread across regions to get allocations quickly. [22:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=1320s)
- Platform automation (an account patch baseline) rebooted new GPU nodes minutes after launch, eating into burst capacity. [23:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=1380s)
- Fine-tuning does not fit tasks that change weekly, need open-ended reasoning or lack labeled data. [7:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=420s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Run fine-tune, quantize and eval-gated deploy as Kubernetes Jobs on the serving cluster, with a GPU-capped Karpenter pool for training. | [12:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=720s) |
| build | Scale vLLM with KEDA on running plus waiting requests and pre-bake model images into GPU node images to cut cold start. | [18:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=1080s) |
| learn | Measure how much GPU memory 4-bit AWQ frees for KV cache on your own model and instance type. | [15:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=900s) |
| write | Publish a fine-tune-versus-prompt decision checklist with your own accuracy and cost numbers. | [7:00](https://www.youtube.com/watch?v=_jb3uLrTa3s&t=420s) |

## Projects mentioned

[vLLM](https://github.com/vllm-project/vllm), [Kubernetes](https://github.com/kubernetes/kubernetes), Karpenter, [KEDA](https://github.com/kedacore/keda), [Prometheus](https://github.com/prometheus/prometheus), Unsloth, Amazon EKS, NVIDIA device plugin
