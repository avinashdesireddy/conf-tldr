# Many Clusters, One GPU Pool: Locality-Aware Scheduling and Data Delivery With Kueue and Dragonfly

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Yiqing Wang (Roblox), Adam Buran (Roblox)  
**Video:** [YouTube](https://www.youtube.com/watch?v=kHbLvCbxslg) (30:52)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Many+Clusters%2C+One+GPU+Pool%3A+Locality-Aware+Scheduling+and+Data+Delivery+With+Kueue+and+Dragonfly)  
**Tags:** `gpu-scheduling`, `multi-cluster`, `kueue`, `data-caching`, `training`

> Roblox joined five Kubernetes clusters across three AWS regions and its own data center into one GPU pool with MultiKueue, a custom external dispatcher and tiered quotas. Dragonfly P2P caching in each cluster turned repeated cross-region S3 reads into local and peer reads for training data and model weights.

## Key points

- Before: one cluster in us-east-1 with a YuniKorn-based scheduler; GPUs sat idle while reserved, jobs were interrupted often, and upgrades hit every training job at once. [0:00](https://www.youtube.com/watch?v=kHbLvCbxslg)
- GPU capacity appeared in different regions with short windows to grab it, while training data stayed in S3 in us-east-1. [1:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=60s)
- They compared YuniKorn, Karmada and MultiKueue; Kueue already had tiers, borrowing and preemption, and MultiKueue extends them across clusters with an external dispatcher hook. [3:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=180s)
- Design principles: stay upstream, isolate cluster failures, users never pick a cluster, fail open if custom parts break, cloud-agnostic job specs. [4:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=240s)
- A hub cluster holds global quota and is the only submission point; jobs set GPU type, priority tier and data region labels, and each spoke's local Kueue checks real node capacity. The first spoke to admit runs the job. [5:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=300s)
- The external dispatcher ranks spokes: hard checks first (framework, GPU type, EFA/RDMA, volumes, full gang fit), then a time-limited preference for the data's region. [7:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=420s)
- Three tiers: guaranteed (owned quota), shared (borrowing idle GPUs) and opportunistic (spot); spokes put guaranteed and shared queues in one cohort so owners can reclaim borrowed GPUs. [9:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=540s)
- On-prem differences (own SKUs, SR-IOV RDMA, separate RDMA stripes, fixed racks) stay in spoke ResourceFlavors, so job specs remain cloud agnostic. [10:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=600s)
- Dragonfly caches S3 objects per cluster: each piece is read from the node's cache, a peer, a seed peer, then S3; if Dragonfly components fail, clients fall back to S3. [14:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=840s)
- A data mobility controller called Fairy pre-stages weights and checkpoints and moves volumes across AZs and regions with the CSI snapshot controller and Velero; they are experimenting with CRIU snapshots for faster LLM inference startup. [17:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=1020s)
- Q&A: cache keys are S3 URLs on dedicated NVMe; LIST and GET authorization always goes to S3, so pods without IAM access cannot read cached data. [22:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=1320s)

## Numbers stated

- Five clusters across three AWS regions plus one on-prem data center; the hub serves about 500 team namespaces. [6:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=360s)
- Each spoke reports free GPU capacity to the hub every 30 seconds. [6:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=360s)
- The gang-fit check blocks about 5,000 partial fits a day. [8:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=480s)
- Data-region preference lasts 5 minutes; almost 9 in 10 jobs still run in their data region. [8:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=480s)
- 80% more useful training work per reserved GPU hour, and 80% fewer job interruptions, versus the old single cluster. [11:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=660s)
- 93% of bytes read were repeat reads; about 15 TB of hot data caused about 3.5 PB of repeat downloads; the top 10 datasets were half of all transfers. [13:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=780s)
- Dragonfly delivered over 9 PB since April: 50% from local cache, 43% from peers, 7% from S3. [15:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=900s)
- Model weight loads about 9x faster; a GLM 5 series model took about 23 minutes from S3 and under 3 minutes once cached. [16:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=960s)
- Over half of workloads now run outside us-east-1. [21:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=1260s)
- Cache TTL is one week on GPU nodes and two weeks on CPU peer nodes. [23:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=1380s)

## Open gaps

- MultiKueue requires identical hub and spoke specs, which breaks with mutating webhooks; they want matching on quota fields only. [18:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=1080s)
- Preemption happens per spoke with no global view, and RayJobs are not validated on the hub, so invalid jobs can hold quota. [19:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=1140s)
- No support for dynamic quota when capacity blocks expire every few weeks. [19:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=1140s)
- Dragonfly caching stays off spot nodes, still needs RDMA support, and lacks a declarative Kubernetes-style API. [20:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=1200s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Use the MultiKueue external dispatcher API to add data-locality and capacity-aware spoke ranking with a fallback timeout. | [7:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=420s) |
| build | Put Dragonfly in front of S3 for training data and model weights after checking access logs for repeat reads. | [13:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=780s) |
| contribute | Help MultiKueue with spec matching under mutating webhooks, global preemption and dynamic quota. | [18:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=1080s) |
| contribute | Add a declarative API and RDMA support to Dragonfly. | [20:00](https://www.youtube.com/watch?v=kHbLvCbxslg&t=1200s) |

## Projects mentioned

[Kueue](https://github.com/kubernetes-sigs/kueue), MultiKueue, Dragonfly, [KubeRay](https://github.com/ray-project/kuberay), [Ray](https://github.com/ray-project/ray), [Kubeflow](https://github.com/kubeflow/kubeflow), Apache YuniKorn, Karmada, Velero, CRIU, SkyPilot, [Kubernetes](https://github.com/kubernetes/kubernetes)
