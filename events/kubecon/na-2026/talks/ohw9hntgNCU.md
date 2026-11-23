# The Latest in GPU, TPU, NIC and Other Device Support - WG Device Management

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** John Belamaric (Google), Morten Jæger Torkildsen (Google)  
**Video:** [YouTube](https://www.youtube.com/watch?v=ohw9hntgNCU) (30:39)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=The+Latest+in+GPU%2C+TPU%2C+NIC+and+Other+Device+Support+-+WG+Device+Management)  
**Tags:** `gpu-scheduling`, `dra`, `device-management`, `kubernetes-core`

> WG Device Management reviewed what Dynamic Resource Allocation (DRA) shipped in Kubernetes 1.37 and what is landing in 1.38, from device taints and extended-resource compatibility to partitionable devices and CPU allocation through DRA. Next up are DRA preemption, gang-aware preemption, richer hardware models and attaching GPUs to running pods.

## Key points

- Device plugins expose an opaque integer count; the working group formed after KubeCon EU 2024 because AI ASICs, RDMA NICs and CXL memory need richer modeling. [1:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=60s)
- DRA has four parts: ResourceSlice to describe devices, ResourceClaim to request them (including under-specified asks like any GPU with 20 GB), the scheduler match, and the kubelet/driver setup. [3:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=180s)
- ResourceSlice is aimed at vendors, ResourceClaim at users and DeviceClass at admins, who can inject policy without changing user manifests. [11:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=660s)
- 1.37: extended resource requests let admins move to DRA drivers while users keep asking for nvidia.com/gpu-style resources. [6:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=360s)
- 1.37: device taints mark a single failing accelerator instead of tainting the whole node and stranding healthy devices. [7:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=420s)
- 1.37 began DRA integration with workload-aware scheduling: resource claims attach to a pod group, plus faster scheduling of many DRA pods at once. [8:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=480s)
- 1.38: partitionable devices (main case NVIDIA MIG), consumable capacity (for example sharing NIC bandwidth), and binding conditions that wait for slow fabric-attached devices and can reschedule on failure. [9:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=540s)
- Node allocatable resources via DRA (beta in 1.38) let CPU, memory and hugepages be allocated in a claim and aligned with the NIC and GPU, with the scheduler avoiding double counting against the container spec. [13:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=780s)
- With workload-aware scheduling, a claim per pod-group replica can allocate a compute domain or TPU slice and clean it up when the replica scales down. [17:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=1020s)
- Adoption needs vendors to ship drivers and ecosystem projects to consume DRA; Karpenter, Cluster Autoscaler and KubeVirt are integrating. [18:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=1080s)
- The DRA plugin is a default kube-scheduler plugin; most new DRA features have a scheduling component. [29:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=1740s)

## Numbers stated

- DRA went GA in Kubernetes 1.34; since 1.36 two to three DRA features graduate to GA each release. [2:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=120s)
- About 20 active features are tracked by the working group at any time. [5:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=300s)
- Placing a NIC and GPU on the same PCIe root can give about 10x the IO performance between them. [12:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=720s)

## Open gaps

- DRA does not yet support preemption; an alpha is targeted for 1.38, and gang-level (workload-aware) preemption comes later. [19:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=1140s)
- Attaching and detaching GPUs on running pods (in-place mutability) is early, possibly alpha in 1.39. [20:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=1200s)
- Components that make their own scheduling decisions, like Kueue and autoscalers, must understand DRA's programmable scheduling; shared importable libraries are being built. [27:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=1620s)
- No public fractional TPU sharing yet. [24:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=1440s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| learn | Follow the working group's live feature tracking sheet and weekly meetings (EU- and US-friendly times). | [21:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=1260s) |
| build | Use a DeviceClass with extended resources to move a cluster to a DRA driver without changing user manifests. | [7:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=420s) |
| contribute | Help autoscalers and admission controllers support newer DRA features such as partitionable devices. | [28:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=1680s) |
| build | Try DRA for non-traditional resources, such as locally cached models or NVMe access, as discussed in Q&A. | [23:00](https://www.youtube.com/watch?v=ohw9hntgNCU&t=1380s) |

## Projects mentioned

[Kubernetes](https://github.com/kubernetes/kubernetes), Dynamic Resource Allocation (DRA), [kube-scheduler](https://github.com/kubernetes/kubernetes/tree/master/pkg/scheduler), [Workload API (pod groups)](https://github.com/kubernetes/enhancements/tree/master/keps/sig-scheduling/4671-gang-scheduling), [LeaderWorkerSet](https://github.com/kubernetes-sigs/lws), [Kueue](https://github.com/kubernetes-sigs/kueue), Karpenter, Cluster Autoscaler, KubeVirt, [HAMi](https://github.com/Project-HAMi/HAMi)
