# Frameworkless ML Serving: Scaling to Thousands of Models with KEDA, Pub/Sub, and Native K8s

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Robin Deaconu (Isomorphic Labs), Neb Jovanovic (Isomorphic Labs)  
**Video:** [YouTube](https://www.youtube.com/watch?v=fAZ-8I62m5s) (31:49)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Frameworkless+ML+Serving%3A+Scaling+to+Thousands+of+Models+with+KEDA%2C+Pub%2FSub%2C+and+Native+K8s)  
**Tags:** `ai-inference`, `autoscaling`, `queues`, `scale-to-zero`, `platform-design`

> Isomorphic Labs moved from Vertex AI to Ray Serve to a framework-free platform where every model is a stateless Kubernetes Deployment pulling from its own Pub/Sub queue behind a stateless gateway. KEDA scales workers to zero, Kubernetes priority and preemption put interactive traffic ahead of batch, and narrow interfaces let them swap storage backends live.

## Key points

- Workloads are framework-agnostic Python inference graphs on GKE; thousands of models share one compute pool, and each prediction holds an accelerator for minutes, not milliseconds. [1:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=60s)
- Vertex AI kept at least one replica per model, so idle cost grew with the catalog. Ray Serve on Kubernetes added a second scheduler, a head node per graph, image rebuilds for resource tweaks, and in-memory requests that scale on concurrency. [3:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=180s)
- Their requirements (any accelerator, no duplicate predictions, scale to zero, interactive preempting batch) mostly described Kubernetes itself, so they built on a stateless worker plus an asynchronous queue. [7:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=420s)
- Request flow: the gateway checks a GCS result store by a hash of input and worker, then a Bigtable status store for pending work, publishes to the worker's Pub/Sub topic, and returns 'pending'. Clients poll with the same request. [9:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=540s)
- Workers pull from their subscription, keep the lease alive while computing, send output to the gateway, and ack after the gateway stores it. [11:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=660s)
- DAGs use 're-enter and check and sleep': a parent that gets 'pending' from a child acks and exits; when the child finishes, the gateway republishes the parent request, which reruns deterministically and now hits the cached result. [13:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=780s)
- A KEDA ScaledObject per worker watches its Pub/Sub backlog, wakes the Deployment from zero to one, and hands off to HPA, which scales by requests per pod. [16:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=960s)
- Each worker priority maps to a Kubernetes PriorityClass; preempting a low-priority pod is safe because its Pub/Sub lease expires and the message is redelivered. [18:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=1080s)
- A small Python SDK hides Pub/Sub, leases, serialization and child calls: researchers subclass a worker and implement handle_message. [20:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=1200s)
- Lessons: start simple, choose high-ceiling primitives, and put every backend behind a narrow interface (factory/strategy pattern) so it can be swapped. A Redis cache in front of GCS evicted keys and caused recomputation; removing it made two of four hot paths slightly faster. [22:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=1320s)
- GitOps acts as the model store: a PR with a short YAML file is compiled by Kapitan into manifests that Argo CD syncs; retiring a model means removing it from Git. [30:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=1800s)

## Numbers stated

- Preemption example: 200 accelerators, two low-priority workers each scaled to 100 pods. [18:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=1080s)
- Gateway scales to thousands of stateless replicas; workers scale from zero to thousands of pods. [19:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=1140s)
- Hashing Redis keys cut per-key memory in half, doubling the in-flight limit. [27:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=1620s)
- Interfaces built in week one still allowed live database swaps three and a half years later. [24:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=1440s)
- Ray-based setup was outgrown about six months in. [6:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=360s)

## Open gaps

- Every model leaves a footprint (subscriptions, ScaledObjects, Deployments); at thousands of models this hits per-project Pub/Sub caps, handled by garbage collection and sharding queues across GCP projects. [28:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=1680s)
- Managed Redis for in-flight status hit its top size tier and connection limit, forcing per-pod connection rationing until a dual-write migration to Bigtable. [27:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=1620s)
- A dedicated model registry will be needed at some point; Git is a stopgap. [30:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=1800s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Serve long-running models as queue-backed stateless workers with KEDA scale-to-zero and PriorityClass-based preemption. | [16:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=960s) |
| build | Put durable result and status stores behind narrow interfaces with in-memory fakes so you can dual-write and flip backends with a config flag. | [27:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=1620s) |
| write | Compare this queue-and-poll design with framework serving (Ray Serve, KServe) for minute-long predictions. | [6:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=360s) |
| learn | The 're-enter and check and sleep' pattern for running DAGs without blocking accelerators. | [13:00](https://www.youtube.com/watch?v=fAZ-8I62m5s&t=780s) |

## Projects mentioned

[Kubernetes](https://github.com/kubernetes/kubernetes), [KEDA](https://github.com/kedacore/keda), Google Cloud Pub/Sub, Cloud Bigtable, Google Cloud Storage, [Redis](https://github.com/redis/redis), [Ray](https://github.com/ray-project/ray), [KubeRay](https://github.com/ray-project/kuberay), Vertex AI, Kapitan, Argo CD
