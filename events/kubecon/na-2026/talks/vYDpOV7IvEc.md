# Deep Dive Into the DRA Driver for NVIDIA GPUs: What Works Today, What’s Coming and Why It Matters

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Shiva Krishna Merla (NVIDIA), Varun Ramachandra Sekar US (Nvidia)  
**Video:** [YouTube](https://www.youtube.com/watch?v=vYDpOV7IvEc) (31:50)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Deep+Dive+Into+the+DRA+Driver+for+NVIDIA+GPUs%3A+What+Works+Today%2C+What%E2%80%99s+Coming+and+Why+It+Matters)  
**Tags:** `gpu-scheduling`, `dra`, `nvidia-gpu`, `gpu-sharing`, `multi-node-nvlink`

> NVIDIA's DRA driver for GPUs already handles time-slicing, MPS, MIG, VM passthrough, health-based device taints and multi-node NVLink through compute domains. The next release adds cross-namespace GPU sharing, several compute-domain pods per node, an always-on IMEX daemon set and beta graduation of most driver features.

## Key points

- The driver has a GPU kubelet plugin, a compute-domain kubelet plugin and a compute-domain controller; it ships as a Helm chart, with features such as MIG and passthrough behind feature gates. [0:00](https://www.youtube.com/watch?v=vYDpOV7IvEc)
- GPU Operator adds a new GPUCluster API that deploys the DRA plugins, DCGM, the DCGM exporter and a validator; it drops the NVIDIA container runtime in favor of CDI and gives monitoring pods admin-access claims. [2:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=120s)
- The GPU Operator DRA mode does not support mixed clusters with the device plugin yet; migration support is planned for an upcoming release. [3:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=180s)
- Sharing today is user-mediated: pods share one ResourceClaim within a namespace. The next release adds system-mediated sharing across namespaces using consumable capacity, with admin-set share counts and no oversubscription. [6:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=360s)
- NVML health events become device taints so the scheduler avoids bad GPUs; next, the DRA resource health status API will show the XID error in pod status. [8:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=480s)
- KubeVirt VMs request a VFIO device class; the driver switches the GPU to the VFIO driver and the DRA downward API tells the VM launcher which GPU it got. [9:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=540s)
- Each GPU is published as both a container device and a VFIO device with the same PCI bus ID; allocating one hides the other, and the partitionable devices API will make this accounting native. [12:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=720s)
- Compute domains run IMEX for multi-node NVLink; today each node allows only channel 0 and one pod, which must take all four GPUs. [17:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=1020s)
- Next release: multiple compute-domain pods per node with unique channels, a ComputeDomainDaemonSet that keeps IMEX running ahead of workloads with clique-by-clique rolling updates, and NVLink between pods on one node, including HGX. [18:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=1080s)
- Demo: a device taint rule with NoExecute simulated an XID failure and the compute-domain workload moved to another node. [23:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=1380s)
- Migration: nvidia.com/gpu requests are turned into DRA claims for full GPUs and MIG (MIG needs a device class per profile); time-sliced and MPS requests cannot be translated yet. [27:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=1620s)

## Numbers stated

- KubeVirt 1.9 added beta support for DRA GPU resources. [9:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=540s)
- Demo node had four GB200 GPUs shared between VMs and pods. [14:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=840s)
- Most Kubernetes DRA feature gates the driver relies on moved to beta in 1.36. [26:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=1560s)

## Open gaps

- Driver features for GPU sharing, health checking and passthrough are still alpha; beta is planned for the next release. [26:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=1560s)
- No straightforward migration from device-plugin time-slicing or MPS to DRA yet. [27:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=1620s)
- Bootstrapping IMEX daemons per workload adds latency at scale, which the daemon set is meant to fix. [18:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=1080s)
- vGPU support is coming next, with MIG-backed vGPU in a later release. [31:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=1860s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| learn | On Kubernetes 1.36 or later, try moving nvidia.com/gpu workloads to DRA via extended-resource translation, starting with full GPUs and MIG. | [27:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=1620s) |
| build | Run VMs and containers on the same GPU nodes using the VFIO device class and KubeVirt. | [14:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=840s) |
| contribute | Test the upcoming ComputeDomainDaemonSet and multi-pod compute domains and send feedback to the driver maintainers. | [25:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=1500s) |
| write | Document topology alignment between the GPU DRA driver and DRANET or the SR-IOV DRA driver for RDMA setups. | [30:00](https://www.youtube.com/watch?v=vYDpOV7IvEc&t=1800s) |

## Projects mentioned

NVIDIA DRA Driver for GPUs, NVIDIA GPU Operator, Dynamic Resource Allocation (DRA), [Kubernetes](https://github.com/kubernetes/kubernetes), KubeVirt, DCGM, Helm, DRANET
