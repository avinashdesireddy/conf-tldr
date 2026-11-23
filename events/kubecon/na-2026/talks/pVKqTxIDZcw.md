# DisaggregatedSet Meets Multi-EPP: Coordinating llm-d at Scale in production

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Mathis Felardos (Mistral AI), Lucas Fernandes Martins (Mistral AI)  
**Video:** [YouTube](https://www.youtube.com/watch?v=pVKqTxIDZcw) (16:18)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=DisaggregatedSet+Meets+Multi-EPP%3A+Coordinating+llm-d+at+Scale+in+production)  
**Tags:** `ai-inference`, `llm-d`, `disaggregated-serving`, `high-availability`, `production`

> Mistral runs llm-d in production and contributed two pieces back: DisaggregatedSet, which manages prefill and decode as one unit inside LeaderWorkerSet, and a cross-replica syncer that lets several endpoint pickers share state so routing scales out.

## Key points

- Disaggregated serving splits compute-bound prefill from memory-bound decode for better service on the same GPUs, but it is hard to operate: rollouts can pair incompatible peers and break the prefill/decode ratio. [1:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=60s)
- LeaderWorkerSet treats a multi-pod replica as one unit (if one pod dies, the group dies) and now supports gang scheduling. [2:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=120s)
- DisaggregatedSet, now part of the LeaderWorkerSet project, declares prefill, decode (and encode) roles with topology-aware placement on NVL72 slices, coordinated progressive rollouts that hold the ratio, and per-role autoscaling. [3:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=180s)
- Cross-revision gating: llm-d shifts traffic to a new revision gradually, only once compatible prefill and decode pods exist. [6:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=360s)
- DisaggregatedSet has been a well-lit path since llm-d v1. [7:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=420s)
- By default the EPP is active-passive: failover means downtime (fail closed) or poor routing (fail open), and the only way to grow is vertically. [8:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=480s)
- Several EPPs without coordination drift apart, each seeing only part of the in-flight load. [9:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=540s)
- The cross-replica syncer is a generic set/get interface; a plugin opts in with about 20 lines of Go by giving the state to sync and an aggregate function. [10:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=600s)
- Mistral's Redis syncer runs every 50 ms in the background, so the request hot path never waits on Redis. [12:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=720s)

## Numbers stated

- Rollouts happen several times a week. [6:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=360s)
- At 300 RPS, three synced EPPs matched the cache hit rate of a single EPP with precise KV-aware routing. [13:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=780s)
- Over 90% of measurements showed zero discrepancy between local and synced state at both 200 and 800 RPS. [14:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=840s)
- One EPP broke down around 700 RPS; three synced EPPs kept serving. [14:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=840s)

## Open gaps

- Safer scale-up during rollouts is still landing (planned for DisaggregatedSet v1.1). [5:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=300s)
- Redis transaction overhead grows with endpoints; a batched-set contribution is in review. [15:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=900s)
- A peer-to-peer syncer that removes Redis entirely is in progress. [15:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=900s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| contribute | Implement another cross-replica syncer backend, or help with the peer-to-peer one. | [15:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=900s) |
| build | Run active-active EPPs with the Redis syncer and load-test past the ~700 RPS single-EPP limit. | [14:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=840s) |
| learn | Try DisaggregatedSet for prefill/decode rollouts instead of hand-managing two Deployments. | [3:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=180s) |
| write | Explain why an active-passive router caps inference scale, using Mistral's numbers. | [8:00](https://www.youtube.com/watch?v=pVKqTxIDZcw&t=480s) |

## Projects mentioned

[llm-d](https://github.com/llm-d/llm-d), [LeaderWorkerSet](https://github.com/kubernetes-sigs/lws), [Redis](https://github.com/redis/redis)
