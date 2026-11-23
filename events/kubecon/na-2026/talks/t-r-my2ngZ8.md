# The Scheduling Stack: Real-World Lessons from Anthropic, Anyscale, Google, and CERN

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Wojciech Tyczyński (Google), Ricardo Rocha (CERN), Kaslin Fields (Google), Decheng Dai (Anthropic), Jui-An Huang (Anyscale)  
**Video:** [YouTube](https://www.youtube.com/watch?v=t-r-my2ngZ8) (33:49)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=The+Scheduling+Stack%3A+Real-World+Lessons+from+Anthropic%2C+Anyscale%2C+Google%2C+and+CERN)  
**Tags:** `scheduling`, `ai-training`, `multi-cluster`, `fragmentation`, `kubernetes-core`

> Big AI users still outgrow the default Kubernetes scheduler, so upstream is turning the scheduling stack into pluggable parts. The hard problems now are fragmentation, multi-cluster onboarding and failures, not raw node count.

## Key points

- Anthropic ran the default kube-scheduler for three years with node selectors and scheduling gates, then built its own about two years ago when gang and topology needs outgrew it. [4:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=240s)
- Anyscale is excited about pod groups and the new Workload API; RL post-training mixes training, inference and data processing in one job. [5:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=300s)
- Google's view: the scheduler is a framework with sane defaults for most users, and every layer (placement, queueing such as Kueue, hardware programming like GPU compute domains or TPU slices, autoscaling) should be replaceable on its own. [9:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=540s)
- CERN runs multi-cluster for capacity, not scale: any team or HPC site that hands over a Kubernetes API endpoint gets onboarded, including GPUs 100 m underground at ALICE. [14:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=840s)
- At Anthropic, cross-cluster pain is above Kubernetes: namespaces, service accounts, RBAC and data locality in each cluster. [17:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=1020s)
- The real limit is workload count and churn, not nodes. Keep one tightly coupled workload in one cluster; use many clusters for many workloads. [19:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=1140s)
- Fragmentation: Anyscale mixes high-priority training with preemptible batch; Anthropic blocks fragmentation at placement and runs a background defrag job. No silver bullet. [23:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=1380s)
- Small workloads that do not fill a node or GPU need attention; CERN published a CNCF reference architecture for it. [28:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=1680s)
- Multi-layer schedulers (Ray on Kubernetes) need better vertical building blocks; the API server and etcd watch path adds latency no fast scheduler can remove. [32:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=1920s)

## Numbers stated

- Anthropic and Google pushed one cluster to 65,000 nodes. [17:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=1020s)
- CERN runs 5,000-node clusters. [14:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=840s)
- Minor scheduler and component tuning for sub-node workloads gave CERN about 30% better performance. [28:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=1680s)

## Open gaps

- The default scheduler still does not meet frontier-lab needs; pluggability is 'not there yet'. [10:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=600s)
- Kubernetes was designed for single-cluster scheduling; multi-cluster needs extra layers each user builds. [16:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=960s)
- Generic checkpoint and restore for non-ML, long-running scientific jobs is still being worked out. [27:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=1620s)
- No standard building blocks to integrate application schedulers (Ray) with Kubernetes scheduling. [32:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=1920s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| learn | Follow the Workload API / pod groups work in SIG Scheduling; it is the upstream answer to gang scheduling. | [5:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=300s) |
| build | Show priority plus preemptible batch sharing one GPU pool (for example with Kueue and Karpenter) and measure cost saved. | [23:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=1380s) |
| write | Compare in-placement anti-fragmentation rules vs background defrag for GPU clusters, using this panel's two approaches. | [24:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=1440s) |
| contribute | Apply CERN's sub-node scheduling reference architecture on another platform and report the result back. | [28:00](https://www.youtube.com/watch?v=t-r-my2ngZ8&t=1680s) |

## Projects mentioned

[Kubernetes](https://github.com/kubernetes/kubernetes), [kube-scheduler](https://github.com/kubernetes/kubernetes/tree/master/pkg/scheduler), [Kueue](https://github.com/kubernetes-sigs/kueue), [Ray](https://github.com/ray-project/ray), [KubeRay](https://github.com/ray-project/kuberay), [Kubeflow](https://github.com/kubeflow/kubeflow), [Workload API (pod groups)](https://github.com/kubernetes/enhancements/tree/master/keps/sig-scheduling/4671-gang-scheduling)
