# Agents Fail. Workflows Recover. Durable Agent Orchestration with Cadence

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Diana Zawadzki (Uber), Shijie Sheng (Uber)  
**Video:** [YouTube](https://www.youtube.com/watch?v=n8t6AblQUMY) (26:14)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Agents+Fail.+Workflows+Recover.+Durable+Agent+Orchestration+with+Cadence)  
**Tags:** `agents`, `durable-execution`, `workflows`, `fault-tolerance`, `production`

> Uber's Cadence team shows how wrapping model and tool calls as Cadence activities lets an agent resume after rate limits or worker crashes instead of starting over. Uber's Agent Executor Service already runs hundreds of thousands of agentic workflows on Cadence, and its execution history pointed straight at the cause of most timeouts.

## Key points

- Each model or tool call is a Cadence activity, a workflow orders them, and a worker runs the code; Cadence records progress in a separate service so a replacement worker can reuse completed results. [1:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=60s)
- Workflows can wait for external input, such as a human decision, or for time to pass. [2:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=120s)
- Smarter models do not prevent disks failing, APIs going down or workers crashing, so systems must assume every component fails. [2:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=120s)
- Common agent failures: rate limits, endless loops, overconfident unsupported conclusions, stalls waiting on human review, and worker process crashes. [3:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=180s)
- Cadence stores only the inputs and outputs of each step; it knows where the workflow is, not the business logic. [6:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=360s)
- Demo: an on-call agent analyzing a checkout 500 error gets rate limited fetching logs, and Cadence retries automatically with configurable retryable and non-retryable error types. [8:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=480s)
- A human sends a guidance signal to the workflow when the first answer has low confidence; the agent replans and traces the error to an exhausted ledger connection pool. [10:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=600s)
- When the worker is killed, a new worker replays the stored history to rebuild state, with no repeated tool calls, and then takes the approval signal. [11:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=660s)
- Workflow reset works as an undo for agents: roll back to a step before a bad decision instead of asking the agent to repair it. [13:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=780s)
- Timeout breakdowns from Cadence observability narrowed the problem to one under-provisioned worker pool. [14:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=840s)
- Q&A: Temporal forked from Cadence; Cadence works with agent sandboxes per activity and sits at the application layer above deployment substrates; avoid hot shards and use continue-as-new for long histories. [18:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=1080s)

## Numbers stated

- Cadence serves over 4,000 use cases at Uber. [4:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=240s)
- The Agent Executor Service, built in July, hosted around 830,000 agentic workflows on Cadence by September. [5:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=300s)
- Service error analyzer: 36,000 runs in 30 days, about 6,000 of them timed out. [6:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=360s)
- In a newer measurement, zero runs of that agent timed out, failed or were terminated. [7:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=420s)
- In the failure-injected demo, Cadence halved model responses and input, output and total tokens, with zero new calls during recovery. [12:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=720s)
- About two-thirds of runs completed, a third timed out, and very few failed. [13:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=780s)
- Over 32,000 runs completed despite at least one earlier failure. [14:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=840s)
- 50% of timeouts came from missing worker responses, another third from activity pickup, and over 99% occurred in one worker pool. [14:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=840s)
- Temporal forked from Cadence in 2019. [18:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=1080s)

## Open gaps

- Built-in guardrail functions are not yet part of the current agent framework integrations. [20:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=1200s)
- Cadence cannot fix workflow logic errors that teams write themselves; those still surface as timeouts. [14:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=840s)
- More agent framework integrations are needed beyond Google ADK and OpenAI Agents; the team asks for contributions. [17:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=1020s)
- Workflow history size is limited, so long-running agents need continue-as-new. [23:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=1380s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| learn | Run the live demo from the Cadence AI samples repo, including the injected failures. | [17:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=1020s) |
| contribute | Add a Cadence integration for another agent framework, or guardrail activities for existing ones. | [17:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=1020s) |
| build | Wrap each model and tool call in an agent as a durable activity with explicit retry policies and a human approval signal. | [16:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=960s) |
| build | Break down agent timeouts by cause (worker response, activity pickup, heartbeat) to find under-provisioned worker pools. | [14:00](https://www.youtube.com/watch?v=n8t6AblQUMY&t=840s) |

## Projects mentioned

Cadence, Michelangelo, Temporal, Google ADK, OpenAI Agents SDK, [Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox)
