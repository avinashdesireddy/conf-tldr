# One Workload to Rule Them All: Workload Aware Scheduling for Distributed AI Training on Kubernetes

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Andrey Velichkevich (Apple)  
**Video:** [YouTube](https://www.youtube.com/watch?v=3O1MewPx8oA) (33:50)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=One+Workload+to+Rule+Them+All%3A+Workload+Aware+Scheduling+for+Distributed+AI+Training+on+Kubernetes)  
**Tags:** `gpu-scheduling`, `gang-scheduling`, `workload-aware-scheduling`, `topology-aware-scheduling`, `ai-training`

> Kubernetes now has Workload, PodGroup and composite PodGroup APIs so kube-scheduler can gang-schedule, preempt and place a whole distributed job instead of single pods. Kubeflow Trainer builds these into TrainJob runtimes so platform admins set gang and topology rules while scientists only write a training function.

## Key points

- Pod-by-pod scheduling deadlocks distributed jobs: two 8-GPU jobs on three 4-GPU nodes can each grab part of the capacity and neither starts. [0:00](https://www.youtube.com/watch?v=3O1MewPx8oA)
- Other gaps: preempting one pod leaves the rest of the gang idle, launcher and worker roles are scheduled as unrelated pods, and placement ignores racks, slowing gradient sync. [2:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=120s)
- Kueue, KAI, Volcano, YuniKorn and the scheduler-plugins project all tackled gang scheduling; a new working group, started about a year ago at KubeCon Japan, aims for one common API. [4:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=240s)
- A PodGroup carries a scheduling policy (gang with a minimum count), topology constraints, a disruption mode and shared resource claims; the scheduler checks the whole group against a cluster snapshot before admitting it. [5:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=300s)
- Preemption has two modes upstream: single (evict one pod) and all (evict the whole pod group). [6:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=360s)
- Composite pod groups express hierarchy with a minimum group count, useful for multi-layer jobs and disaggregated prefill/decode inference. [7:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=420s)
- Kubeflow Trainer splits personas: admins define runtimes with zone/block/rack levels of scheduling policy; scientists call a Python SDK; JobSet and LeaderWorkerSet run underneath. [10:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=600s)
- The same scheduling fields are meant to appear in TrainJob, JobSet and LeaderWorkerSet so users get one experience across workload types. [14:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=840s)
- Kind demo: without gang scheduling a 5-pod job ran 4 pods and blocked a smaller job; with a gang policy the big job waited, the small one ran, and events named the unmet min count. A rack constraint kept each job in one rack. [19:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=1140s)
- TrainJob can report progress and ETA from framework callbacks; the speaker proposes using it for backfill and for preempting jobs that will finish later. [24:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=1440s)
- Kueue stays on top for quotas, cluster queues and multi-cluster; its topology-aware scheduling overlaps with the new upstream work and the two are being aligned. [31:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=1860s)

## Numbers stated

- Workload and PodGroup APIs are beta in Kubernetes 1.37; composite pod groups are alpha with beta expected in 1.38 and GA hoped for 1.40. [22:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=1320s)
- Trainer integration with composite pod groups is planned for Trainer 2.5, about two months out. [23:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=1380s)
- Demo cluster: 4 nodes across 2 racks; the first job asked for 5 pods. [16:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=960s)

## Open gaps

- Deep topology across multiple composite pod groups is slow for kube-scheduler; performance work is ongoing so 1,000 pods do not take an hour to schedule. [29:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=1740s)
- How Kueue's topology-aware scheduling hands off to the scheduler's own version is still being worked out, so the two will overlap for a while. [31:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=1860s)
- Topology is label-based only; health-aware topology (hardware degraded by heat or cooling failures) is an open issue. [32:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=1920s)
- Volcano maintainers are not yet engaged in the API design; the speaker asked them to join. [27:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=1620s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| learn | Try the beta Workload and PodGroup APIs on a kind cluster with a gang policy and a rack constraint, as in the demo. | [21:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=1260s) |
| contribute | Bring Volcano or other scheduler use cases to the workload-aware scheduling working group and Trainer calls. | [27:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=1620s) |
| build | Prototype backfill or ETA-aware preemption using TrainJob's reported progress and ETA. | [25:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=1500s) |
| contribute | Adopt the shared scheduling fields in your own workload controller so it composes pod groups like TrainJob and JobSet. | [14:00](https://www.youtube.com/watch?v=3O1MewPx8oA&t=840s) |

## Projects mentioned

[Kubernetes](https://github.com/kubernetes/kubernetes), [kube-scheduler](https://github.com/kubernetes/kubernetes/tree/master/pkg/scheduler), [Workload API (pod groups)](https://github.com/kubernetes/enhancements/tree/master/keps/sig-scheduling/4671-gang-scheduling), [Kubeflow](https://github.com/kubeflow/kubeflow), [Kueue](https://github.com/kubernetes-sigs/kueue), [Volcano](https://github.com/volcano-sh/volcano), [KAI Scheduler](https://github.com/kai-scheduler/KAI-Scheduler), [LeaderWorkerSet](https://github.com/kubernetes-sigs/lws), JobSet, Apache YuniKorn, Slurm, PyTorch, JAX, Dynamic Resource Allocation (DRA)
