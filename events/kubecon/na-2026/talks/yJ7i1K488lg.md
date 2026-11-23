# Securing the Agentic Future: Distributing LLM Weights and Sandboxed AI Agents via Harbor

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Chenyu Zhang (VMware by Broadcom), Yan Wang (Broadcom)  
**Video:** [YouTube](https://www.youtube.com/watch?v=yJ7i1K488lg) (28:23)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Securing+the+Agentic+Future%3A+Distributing+LLM+Weights+and+Sandboxed+AI+Agents+via+Harbor)  
**Tags:** `agent-security`, `supply-chain`, `model-distribution`, `oci-artifacts`, `sandboxing`

> An AI agent ships as two things, model weights and the sandbox it acts in, and today neither goes through the supply chain teams already use for container images. The talk shows Harbor storing weights as ModelPack OCI artifacts and agent images with a sandbox permission descriptor, so both get the same scanning, signing, replication and admission policy.

## Key points

- An agent is a model, instructions, a runtime loop and tools; five of those six pieces already ship as OCI images, but model weights are usually loose Hugging Face files with no digest or signature. [4:00](https://www.youtube.com/watch?v=yJ7i1K488lg&t=240s)
- Typical practice: weights downloaded onto a VM, PVC or S3 bucket with no revision pinning or scanning, which fails outright in air-gapped clusters; agent tools are pulled from the internet at runtime with no policy. [5:00](https://www.youtube.com/watch?v=yJ7i1K488lg&t=300s)
- Target state: one registry (Harbor) and two artifact types, models as ModelPack artifacts and agents plus tools as plain OCI images, inside one trust boundary. [5:00](https://www.youtube.com/watch?v=yJ7i1K488lg&t=300s)
- ModelPack (CNCF sandbox) defines a model as an OCI artifact: a model config with architecture, parameters, precision and license, plus typed layers for weights, tokenizer config and docs. The modctl CLI builds, pushes and pulls them like Docker. [7:00](https://www.youtube.com/watch?v=yJ7i1K488lg&t=420s)
- Spec recommendations: one weight file per layer so parallel and P2P pulls work, and leave weights uncompressed because gzip gains nothing on near-random data. [9:00](https://www.youtube.com/watch?v=yJ7i1K488lg&t=540s)
- Harbor shows model metadata natively and adds Hugging Face model sync: register an endpoint and token, create a sync policy, and Harbor pulls a revision and republishes it as ModelPack. It is model-aware sync, not a proxy cache. [11:00](https://www.youtube.com/watch?v=yJ7i1K488lg&t=660s)
- Once in Harbor, models get a model scanner (e.g. flagging pickle files that run code on load), SBOMs, Cosign signing and a rule to refuse unsigned artifacts. [12:00](https://www.youtube.com/watch?v=yJ7i1K488lg&t=720s)
- Distribution: a central Harbor replicates to regional Harbors, and Dragonfly P2P lets nodes share per-file layers so the registry serves a model once. [13:00](https://www.youtube.com/watch?v=yJ7i1K488lg&t=780s)
- Pods mount the model with Kubernetes image volumes, pinned by digest; admission policy must cover image volumes, not just containers. The demo synced a model from Hugging Face and served it from a Harbor-backed image volume. [15:00](https://www.youtube.com/watch?v=yJ7i1K488lg&t=900s)
- Docker's experimental sandbox kit spec attaches a descriptor to the agent image listing allowed network destinations, credentials and writable paths; pinning the agent by digest also pins its permissions. [22:00](https://www.youtube.com/watch?v=yJ7i1K488lg&t=1320s)
- Admission then allows registry pulls only from Harbor, verifies signatures on agent and model, and the sandbox enforces egress to only Harbor and the inference server. [26:00](https://www.youtube.com/watch?v=yJ7i1K488lg&t=1560s)

## Open gaps

- The sandbox kit spec has no final version yet, and today only Docker's sandbox runtime reads the descriptor. [23:00](https://www.youtube.com/watch?v=yJ7i1K488lg&t=1380s)
- ModelPack support in Harbor is still a community proposal targeted at the next release. [28:00](https://www.youtube.com/watch?v=yJ7i1K488lg&t=1680s)
- Each agent tool (Codex, Claude Code, Cursor) defines what an agent may touch in its own way, outside the artifact. [21:00](https://www.youtube.com/watch?v=yJ7i1K488lg&t=1260s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Package model weights with modctl as ModelPack artifacts and mount them in pods via digest-pinned image volumes instead of init-container downloads. | [15:00](https://www.youtube.com/watch?v=yJ7i1K488lg&t=900s) |
| build | Extend admission policy to verify signatures on image volumes and restrict model and agent pulls to your own registry. | [15:00](https://www.youtube.com/watch?v=yJ7i1K488lg&t=900s) |
| contribute | Review the Harbor ModelPack proposal and help sandbox runtimes adopt the sandbox kit descriptor once it is donated to CNCF. | [24:00](https://www.youtube.com/watch?v=yJ7i1K488lg&t=1440s) |
| learn | Model-specific scanning risks such as pickle files that execute code on load, which CVE scanners miss. | [12:00](https://www.youtube.com/watch?v=yJ7i1K488lg&t=720s) |

## Projects mentioned

Harbor, ModelPack, modctl, Dragonfly, Cosign, Hugging Face, [Kubernetes](https://github.com/kubernetes/kubernetes), [vLLM](https://github.com/vllm-project/vllm), Ollama, Docker
