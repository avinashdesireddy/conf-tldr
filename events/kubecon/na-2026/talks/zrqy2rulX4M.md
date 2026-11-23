# The Seams Are the Trap: Agent Fleets from CNCF Parts You Already Have

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Aleksander Slominski (IBM), Mariusz Sabath (IBM)  
**Video:** [YouTube](https://www.youtube.com/watch?v=zrqy2rulX4M) (27:23)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=The+Seams+Are+the+Trap%3A+Agent+Fleets+from+CNCF+Parts+You+Already+Have)  
**Tags:** `agents`, `event-driven`, `autoscaling`, `audit`, `agent-security`

> IBM speakers built a headless agent fleet from existing CNCF parts: KEDA scales agent runners from Kafka lag, CloudEvents carry the tasks, and a small Python glue layer bridges HTTP and Kafka. Events are signed and kept in order, so the Kafka log doubles as a verifiable audit trail, while agent identity with SPIFFE/SPIRE is still unsolved.

## Key points

- Premise: instead of buying an agent platform, compose components many clusters already run (KEDA, Kafka via Strimzi, CloudEvents) and add only thin glue code. [0:00](https://www.youtube.com/watch?v=zrqy2rulX4M)
- KEDA scales on consumer lag, the work left in a Kafka topic, so agent runners scale to zero when idle; cooldown settings stop scale-down from flapping. [4:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=240s)
- Their added parts: an event bridge that turns HTTP requests into Kafka events and Kafka events back into notifications, and event runners that consume tasks, start agents and publish agent output back to Kafka. [6:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=360s)
- Events are signed when the bridge accepts them; the runner checks the signature and that the agent may consume the event before it starts the agent. [10:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=600s)
- Kafka keeps the signed event sequence, so the log works as an audit trail that can show lost or injected events. The last event of a run, the terminal event, records the result. [10:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=600s)
- Kafka partitions keep events in order per consumer, which suits stateful, long-running agents that receive several inputs. [14:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=840s)
- Runs are labeled as groups so a batch of many agents produces one start and one finish notification instead of one per agent. [17:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=1020s)
- Demo: Claude Code in headless mode, using an event bridge skill, submits one task and then a batch of 100. Results arrive on a phone through ntfy with an HTML view of the run. [18:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=1080s)
- The audit tool verifies signatures and terminal events; an unsigned event injected directly into Kafka is rejected by the agent runner. [23:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=1380s)
- Everything is in Python, with specifications in their GitHub repo so it can be rebuilt in another language. [9:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=540s)
- Q&A: not an anti-vendor talk; the speaker expects pluggable library pieces on top of KEDA and Kafka rather than one sold platform. [26:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=1560s)

## Numbers stated

- Demo batch of 100 agents across 12 Kafka partitions, with KEDA capped at 10 runner pods. [22:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=1320s)
- A single agent run produced 16 events, mostly internal Claude events. [20:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=1200s)
- The task lifecycle in the demo has seven steps, from submission to scale back to zero. [12:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=720s)
- Scaling back down after the batch took about two to three minutes. [23:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=1380s)

## Open gaps

- SPIFFE/SPIRE ties identity to a pod, but an agent's identity shifts as it gains skills and plugins at runtime; they have only a simple workaround. [11:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=660s)
- Changing who may consume events is not dynamic: runners are scaled to zero and reconfigured. [12:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=720s)
- KEDA scale-up is not instant, so large batches wait while runners start. [21:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=1260s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Put signed CloudEvents and signature checks in front of agents you trigger from a queue, and verify the event log as an audit trail. | [10:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=600s) |
| build | Scale headless agent workers from queue lag with KEDA, including scale to zero. | [4:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=240s) |
| contribute | Work on dynamic agent identity that reflects loaded skills and plugins, beyond pod-level SPIFFE IDs. | [11:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=660s) |
| learn | Kafka partitions, consumer offsets and lag, and how they give ordering and crash recovery for agent tasks. | [16:00](https://www.youtube.com/watch?v=zrqy2rulX4M&t=960s) |

## Projects mentioned

[KEDA](https://github.com/kedacore/keda), Apache Kafka, Strimzi, CloudEvents, SPIFFE, SPIRE, [Kubernetes](https://github.com/kubernetes/kubernetes), Claude Code, ntfy
