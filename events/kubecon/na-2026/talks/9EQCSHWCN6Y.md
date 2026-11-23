# Beyond the Cluster Boundary: Sharing GPUs at Scale

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Tim Killian (Snapchat)  
**Video:** [YouTube](https://www.youtube.com/watch?v=9EQCSHWCN6Y) (25:10)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Beyond+the+Cluster+Boundary%3A+Sharing+GPUs+at+Scale)  
**Tags:** `gpu-scheduling`, `multi-cluster`, `gpu-utilization`, `quota-management`

> Snap pooled its reserved GPUs into capacity-pool clusters and lets workloads in thousands of customer clusters reach them through virtual nodes built on Virtual Kubelet, with Kueue gating access and handling borrowing and preemption. Average reservation occupancy in its largest region rose from under 50% to over 90%, saving tens of millions of dollars a year.

## Key points

- The approach applies to any constrained compute when you must run more than one cluster, whether for scale or compliance. [0:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y)
- Inference reservations were sized for peak, so average occupancy stayed under 50%; lending to batch was possible but owners could not reclaim GPUs without paging someone, so teams walled off their reservations. [1:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=60s)
- Capacity is grouped by machine type into cell clusters, but deployments cannot be placed there directly because inference falls back across machine types (G4, then G2, then C4D) at runtime. [4:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=240s)
- Two building blocks: a virtualization layer separating where deployments live from where capacity runs, and workload-level quotas (for example many inference partitions sharing one quota), while keeping teams' operational model. [5:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=300s)
- Virtual nodes built on Virtual Kubelet copy a bound pod's ConfigMaps, Secrets and the pod itself to the remote pool cluster and mirror status, so logs and exec work as usual. [8:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=480s)
- Kueue in each customer cluster gates access to virtual nodes by quota; without quota, pods fall back to the cluster's normal autoscaling (Karpenter, cluster autoscaler, compute classes). [9:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=540s)
- MultiKueue was not used for autoscaled inference because HPA needs node metrics from the metrics server; it is planned for some batch workloads. [11:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=660s)
- In the pool cluster, vanilla Kueue has the global view and handles cohort borrowing and preemption; customer clusters are shown their entitlement plus anything borrowable, including capacity held by lower-priority borrowers. [13:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=780s)
- During a cloud provider outage, central quota changes chose which critical workloads kept GPUs and the rest drained on their own, with no ad-hoc paging. [15:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=900s)
- Next: more constrained machine types and opt-in cross-region failover that joins virtual nodes just in time when local and on-demand capacity is exhausted. [16:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=960s)
- Each virtual node represents only homogeneous machines in one topology domain, so topology-aware scheduling and compact placement still work; the number of nodes behind one virtual node is set by blast radius. [23:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=1380s)

## Numbers stated

- Snap runs thousands of Kubernetes clusters with over 100,000 machines across multiple clouds and regions. [0:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y)
- Average reservation occupancy in the largest region went from under 50% to over 90%. [14:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=840s)
- Savings of tens of millions of dollars in annual compute costs. [14:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=840s)
- A cloud provider outage removed over 20% of reservations over a few days. [15:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=900s)

## Open gaps

- MultiKueue breaks HPA-driven inference because there is no node in the metrics loop. [11:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=660s)
- The design assumes a flat network with reachable pod IPs; operators that use their own networking APIs must be checked case by case. [22:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=1320s)
- Cross-cloud failover has only been proven as a proof of concept and needs an interconnect. [21:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=1260s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Prototype a Virtual Kubelet provider that mirrors pods and their ConfigMap/Secret dependencies into a shared GPU pool cluster. | [9:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=540s) |
| build | Pair per-cluster Kueue quotas with a central Kueue cohort and advertise entitlement plus borrowable capacity. | [13:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=780s) |
| contribute | Explore how MultiKueue could support HPA-scaled deployments that need in-cluster metrics, the gap that kept Snap on virtual nodes. | [11:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=660s) |
| write | Write up using central quota changes to drain lower-priority GPU work during capacity loss. | [15:00](https://www.youtube.com/watch?v=9EQCSHWCN6Y&t=900s) |

## Projects mentioned

[Kubernetes](https://github.com/kubernetes/kubernetes), Virtual Kubelet, [Kueue](https://github.com/kubernetes-sigs/kueue), MultiKueue, Karpenter, Cluster Autoscaler, Horizontal Pod Autoscaler
