# Reduce vLLM Pod Cold Starts with KServe Kernel Caching

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Jooho Lee (Red Hat), Vishwa Hiren Gandhi (Oracle)  
**Video:** [YouTube](https://www.youtube.com/watch?v=v1o70EZXaZY) (31:11)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Reduce+vLLM+Pod+Cold+Starts+with+KServe+Kernel+Caching)  
**Tags:** `ai-inference`, `cold-start`, `kserve`, `caching`, `supply-chain`

> Even with model weights cached, each new vLLM pod recompiles its GPU kernels. KServe now captures those compiled artifacts, publishes them as signed OCI images, and lets new pods reuse them, cutting compile time from about 35 seconds to about 1 second in their tests.

## Key points

- KServe turns a ServingRuntime and an InferenceService into a Deployment; a storage initializer downloads the model, then vLLM loads it and initializes before the pod is ready. [2:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=120s)
- vLLM startup steps: model loading, graph compilation, CUDA graph capture, and engine initialization (memory profiling, KV cache allocation). [3:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=180s)
- A new replica on another node does not inherit compiled artifacts and repeats every startup step. Model download can be avoided with KServe's local model cache; kernel compilation is the focus here. [5:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=300s)
- Compiling at runtime fits the code to the actual GPU architecture, tensor shapes, data types and vLLM/PyTorch/CUDA versions. vLLM already saves compiled artifacts to a cache directory, but ephemeral pod storage loses them. [7:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=420s)
- Shared NFS (ReadWriteMany) adds a storage dependency during burst scale-out, and node-local caches must be copied between nodes. Since the cache is executable code, its origin must be trusted. [9:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=540s)
- The approach: package compiled artifacts as an OCI image, push to a registry, sign it, verify the signature before reuse, and prefetch onto GPU nodes. [10:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=600s)
- This began as a separate GPU Kernel Manager (GKM) project using persistent volumes; in KServe it moved to OCI images for portability and signing. The feature is optional. [11:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=660s)
- Cache selection uses a workload footprint (workload, runtime image, model) and a compatibility footprint (data type, compile settings). It prefers the same workload, then a compatible one, else compiles and captures a new cache. [13:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=780s)
- vLLM logs confirmed the precompiled AOT artifacts were loaded, so the gain came from real cache reuse. [18:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=1080s)
- On a fresh GPU node, pulling the runtime image took longer than the rest of vLLM startup after cache reuse. Next idea: prefetch the runtime image and kernel cache onto new GPU nodes ahead of time (not yet measured end to end). [22:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=1320s)
- Q&A: unlike GPU snapshotting, this needs no special device or fast GPU-to-GPU network; it uses OCI images, registries and cosign with cert-manager, and works in disconnected clusters. [27:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=1620s)

## Numbers stated

- Baseline vLLM startup is about 250 seconds, excluding image pull and model download. [4:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=240s)
- Model loading takes about 142 seconds (57%), compilation 35 seconds (14%), CUDA graph capture 12 seconds, 52 seconds of bootstrap and 9 seconds of API startup. [5:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=300s)
- Test setup: Qwen2.5 32B with AWQ quantization on an NVIDIA L40S GPU. [15:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=900s)
- Cache capture added no penalty: about 160 seconds versus 169 seconds for local model alone. [17:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=1020s)
- With cache reuse, startup dropped from 160 to 110 seconds and compile time from about 35 to 1.16 seconds, a 96% reduction. [18:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=1080s)
- Engine initialization dropped from about 55 to 18 seconds. [18:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=1080s)
- Full pod startup on a fresh GPU node was about 11 minutes standard and about 3 minutes with a local model; model loading to GPU still took 128 seconds. [21:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=1260s)
- Pulling the runtime image on a new GPU node took about 157 seconds. [22:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=1320s)

## Open gaps

- Model loading into GPU memory remains the largest startup cost and is not addressed by kernel caching. [6:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=360s)
- Runtime image pull on new GPU nodes can exceed the remaining startup time; image prefetch is proposed but not measured end to end. [23:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=1380s)
- Changing compilation options invalidates the cached image, so the cache must be rebuilt. [26:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=1560s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| learn | Measure your full cold start by stage (image pull, download, loading, compile, CUDA graphs) before choosing what to cache. | [23:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=1380s) |
| build | Enable KServe kernel caching with signed OCI artifacts alongside local model caching for vLLM services that scale out often. | [12:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=720s) |
| build | Prefetch runtime images and kernel caches onto new GPU nodes before pods are scheduled. | [23:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=1380s) |
| write | Compare kernel caching with GPU snapshotting for cold starts, covering hardware requirements and trust. | [27:00](https://www.youtube.com/watch?v=v1o70EZXaZY&t=1620s) |

## Projects mentioned

[KServe](https://github.com/kserve/kserve), [vLLM](https://github.com/vllm-project/vllm), [llm-d](https://github.com/llm-d/llm-d), LMCache, GPU Kernel Manager, PyTorch, cosign, cert-manager, [Kubernetes](https://github.com/kubernetes/kubernetes)
