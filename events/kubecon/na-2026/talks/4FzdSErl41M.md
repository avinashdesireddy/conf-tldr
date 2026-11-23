# Groundhog Pod: Scaling AI Inference with Kata Pod Snapshots

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** David Justice (Microsoft), Roaa Sakr (Microsoft)  
**Video:** [YouTube](https://www.youtube.com/watch?v=4FzdSErl41M) (27:54)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Groundhog+Pod%3A+Scaling+AI+Inference+with+Kata+Pod+Snapshots)  
**Tags:** `ai-inference`, `cold-start`, `snapshots`, `kata-containers`, `gpu`

> Microsoft extended Kata Containers and Cloud Hypervisor to snapshot a whole pod VM, including GPU state captured with CUDA checkpoint, after the model is loaded. Restoring from the snapshot cut a demo inference pod's time to first response from about 34 seconds to about 11.

## Key points

- Slow inference pod startup (image pull, loading Python, PyTorch and CUDA, loading weights, warm-up) costs money while serving nothing. [1:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=60s)
- Startup latency sets how many warm pods you keep in reserve for spikes; faster startup means a smaller buffer. [4:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=240s)
- CRIU checkpoints a process and its memory but not kernel state. Kata runs each pod in a lightweight VM with its own guest kernel, so a VM snapshot captures application, CPU, memory and kernel state together. [5:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=300s)
- Snapshots fail to restore across CPU microarchitectures; a virtual CPU profile with a minimum feature set lets a snapshot taken on one CPU generation restore on another, leaving GPU compatibility as the main constraint. [7:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=420s)
- GPU memory and execution state are captured with CUDA checkpoint into guest RAM, and then the whole VM is snapshotted to a storage back end. [8:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=480s)
- Restore: an annotation on the pod tells the Kata runtime to start the VM from the snapshot, then CUDA checkpoint restores and unlocks the GPU. [10:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=600s)
- Demo with a Pythia text-generation model: after snapshotting, the running pod resumed inference, was terminated, and a new pod restored from the snapshot answered in about 11 seconds. [11:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=660s)
- From the snapshot, the software and model loading steps are skipped; GPU warm-up takes slightly longer. [14:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=840s)
- Snapshots also help with traffic spikes, worker failures, quiet periods, group and batch jobs, Java JIT warm-up, and ML training, where a demo resumed the loss curve after restoring a mid-training snapshot. [19:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=1140s)
- Some Cloud Hypervisor changes are upstream; Kata snapshot and restore design is in progress, with plans to align with open KEPs in SIG Node and containerd work on snapshot/restore. [22:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=1320s)
- Q&A: no cross-architecture restore (for example ARM to AMD64); same-architecture restore works on tested SKUs and depends on the CPU feature profile, and GPU compatibility will be limited at first. [24:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=1440s)

## Numbers stated

- Demo cold start took about 33 to 34 seconds to a response; restore from snapshot took about 11 seconds, about a 65% improvement. [13:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=780s)
- Loading software and model took about 21 seconds cold versus 5 seconds from a snapshot. [14:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=840s)
- CPU-only restores reach sub-second restart times in their lab. [15:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=900s)
- A simulation with pay-as-you-go H200 pricing saved about $30 over 3 minutes 45 seconds of spiky traffic. [18:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=1080s)

## Open gaps

- The demo pins to and restores on a single GPU; restoring across GPUs needs more work. [21:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=1260s)
- Results were on a modest GPU with no optimizations; restore speed, CUDA recovery paths and snapshot size still need tuning on production hardware. [15:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=900s)
- Protecting snapshots in multi-tenant clusters and using confidential containers to hide models from the infra provider are open. [22:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=1320s)
- GPU compatibility between snapshot and restore hosts is a big unresolved question. [25:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=1500s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| contribute | Join the upcoming upstream Kata snapshot and restore design work announced on the Kata Slack. | [23:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=1380s) |
| learn | Follow the SIG Node KEPs and containerd proposals for snapshot/restore that Kata plans to integrate with. | [23:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=1380s) |
| build | Model your warm-pod buffer as a function of startup latency to estimate savings from faster restores. | [17:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=1020s) |
| build | Test mid-training VM snapshots as a way to survive evictions and maintenance without restarting jobs. | [20:00](https://www.youtube.com/watch?v=4FzdSErl41M&t=1200s) |

## Projects mentioned

Kata Containers, Cloud Hypervisor, CRIU, containerd, [Kubernetes](https://github.com/kubernetes/kubernetes), PyTorch
