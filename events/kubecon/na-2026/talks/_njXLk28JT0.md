# Quota Isn't Enough: Topology Aware Scheduling on Modern GPU Clusters

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Amy Chen (CoreWeave), JJ Jordan (Cohere)  
**Video:** [YouTube](https://www.youtube.com/watch?v=_njXLk28JT0) (35:14)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Quota+Isn%27t+Enough%3A+Topology+Aware+Scheduling+on+Modern+GPU+Clusters)  
**Tags:** `gpu-scheduling`, `topology-aware-scheduling`, `kueue`, `training`, `fragmentation`

> On NVL72 racks the NVLink domain is the whole rack, and leaving it drops bandwidth 18x, so having GPU quota no longer means a job will run fast or start at all. The speakers explain Kueue Topology Aware Scheduling and production lessons on test pods, slice sizing, node hot swap, preemption tickets, fragmentation and hero workloads.

## Key points

- A training collective runs at the speed of its slowest link; with NVL72, staying inside a rack keeps all traffic on NVLink, while the default scheduler and quota never ask where pods land. [0:00](https://www.youtube.com/watch?v=_njXLk28JT0)
- Placing 9 GPUs on one rack and 7 on another makes every all-reduce round cross the network, though quota and scheduling look identical to Kubernetes. [4:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=240s)
- Training wants powers of two, so jobs use 64 of each rack's 72 GPUs; without telling Kueue 64 is the unit, a 128-GPU job can land as 72 + 56. [6:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=360s)
- TAS config: the platform declares a Topology (e.g. fabric, superpod, leaf group, NVLink domain, node) on a ResourceFlavor; users add one pod-template annotation; Kueue checks quota and shape at admission and pins pods with node selectors. [8:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=480s)
- CoreWeave's idle-node verification pods blocked customer jobs once TAS counted them; fix was no Kueue queue label, the unconstrained topology annotation, and priority -1 so kube-scheduler preempts them. [10:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=600s)
- Multi-rack jobs need a slice size (16 nodes of 4 GPUs = 64 GPUs per rack) for balanced placement; jagged allocations hurt speed and have triggered XLA crashes. [12:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=720s)
- Annotation modes: unconstrained (inference, single-node), preferred (best effort, may land unbalanced, for post-training), required (wait for the right shape, for pre-training). [13:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=780s)
- Node hot swap via the TAS failed-node-replacement feature gate replaces one pinned node within the same topology instead of re-queuing the whole job. Kueue only sees taints, set at CoreWeave by Node Problem Detector and verification tests. [16:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=960s)
- Preemption tickets: Kueue preempts only if the pending job would fit after evictions, so quota math alone misleads users. [19:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=1140s)
- Fragmentation: job departures leave holes that do not align with racks; best-fit, least-capacity and balanced placement only slow the decay, since nothing moves running work. [20:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=1200s)
- Cohere fills spare rack nodes with preemptible inference via cohorts with quota borrowing, keeping hot spares for the largest jobs. For hero jobs, CoreWeave built a stop-gap rack-clearing controller; upstream Kueue now has configurable preemption that treats topology plus priority as a reason to preempt. [24:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=1440s)

## Numbers stated

- Bandwidths: memory 8 TB/s, NVLink 5 900 GB/s, host 450 GB/s, PCIe 64 GB/s, InfiniBand across racks 50 GB/s. [2:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=120s)
- In-rack bandwidth is 18x faster than between racks on NVL72; on H100 the off-node drop was about 4.5x. [5:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=300s)
- About $18,000 per day for one rack at published on-demand CoreWeave pricing. [5:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=300s)
- NCCL all-reduce, 8 GB messages on four GB200 nodes: 908 GB/s bus bandwidth within a single rack. [6:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=360s)
- Racks are delivered once 16 of 18 nodes are healthy; 64 of 72 GPUs are promised, 8 are failure allowance. [7:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=420s)
- Hero workload example: 1,000 GPUs at highest priority. [25:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=1500s)

## Open gaps

- Nothing in the system can defragment running work; admission policies only slow fragmentation. [23:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=1380s)
- Kueue only understands taints, so faults that pass every automated check (some NVLink degradation) put pods back on the same bad node repeatedly. [18:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=1080s)
- Kueue picks nodes and kube-scheduler places pods, so they can race; moving topology into kube-scheduler via workload-aware scheduling is future work. [29:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=1740s)
- Configurable preemption moves preemption to a global level, so who may defragment must be tightly controlled; wider defragmentation needs more work. [30:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=1800s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Set required topology with slice sizes for pre-training jobs and preferred for post-training on rack-scale GPU clusters. | [14:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=840s) |
| build | Wire GPU health signals (XID errors, NVLink faults, failed NCCL tests) into node taints so Kueue's failed-node replacement can act. | [17:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=1020s) |
| contribute | Work on Kueue defragmentation and moving topology awareness into kube-scheduler. | [29:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=1740s) |
| write | Build a dashboard that shows topology-aware free capacity per rack, not just quota, to answer 'why is my job pending'. | [19:00](https://www.youtube.com/watch?v=_njXLk28JT0&t=1140s) |

## Projects mentioned

[Kueue](https://github.com/kubernetes-sigs/kueue), [Kubernetes](https://github.com/kubernetes/kubernetes), [kube-scheduler](https://github.com/kubernetes/kubernetes/tree/master/pkg/scheduler), NCCL, Node Problem Detector, XLA
