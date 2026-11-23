# Agents on the Platform: Four Perspectives on the Conversation We're Already Having in Private

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Kasper Borg Nissen (Dash0), Juraci Paixão Kröhling (OllyGarden), Joseph Sandoval (Adobe), Jed Salazar (Edera), Alexa Griffith (Red Hat)  
**Video:** [YouTube](https://www.youtube.com/watch?v=oWFO88oAHOY) (31:12)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Agents+on+the+Platform%3A+Four+Perspectives+on+the+Conversation+We%27re+Already+Having+in+Private)  
**Tags:** `agents`, `platform-engineering`, `observability`, `agent-security`, `identity`

> A panel with platform, OpenTelemetry, security and inference perspectives discusses what platform teams must provide to run agents: sandboxing, identity, observability and inference routing. The shared advice is to rely on maturing community projects, treat agents as adversarial, instrument them from within, and learn the stack hands-on before rushing.

## Key points

- Sandbox runtimes are now commodity; build your own only for differentiated needs such as regulated environments or special file system access. [3:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=180s)
- Agent lifecycle raises new ownership questions, such as which identity an agent takes when it resumes after suspension. [5:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=300s)
- Security view: agent workloads should be considered adversarial, and standard containers are not an isolation boundary; use micro VMs without a shared kernel. [6:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=360s)
- For inference, agents are long-running and bursty, so routing must reach the GPU that holds the cached context to avoid paying for uncached tokens. [8:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=480s)
- HTTP 200 does not mean an agent did its job; compare routing guesses (e.g. llm-d prefix routing) with what actually happened, across multiple turns. [10:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=600s)
- External observation is not enough for agents; they need instrumentation from within, like business instrumentation in microservices. [11:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=660s)
- Many agent frameworks now conform to OpenTelemetry GenAI semantic conventions, but these are not yet stable because the underlying protocols keep changing. [13:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=780s)
- Tracing has become the default signal for agents, covering tool calls and MCP calls. [15:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=900s)
- Per-agent identity via SPIFFE/SPIRE is preferable to shared service accounts or human identities; egress network policy or proxying is the best value control. [17:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=1020s)
- Object capabilities: a proxy outside the micro VM holds the token and performs authentication, so the agent gets granular capabilities and no ambient credential. [20:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=1200s)
- Auditing requires tracing delegated authority through sub-agents; context propagation across A2A and MCP is hard to get right. [23:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=1380s)

## Numbers stated

- OpenAI reportedly spent about $1 million on tokens and found around 900 local privilege escalation vulnerabilities in the Linux kernel. [6:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=360s)
- Running llm-d in production may need two clusters with about 250 GPUs each for redundancy. [29:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=1740s)

## Open gaps

- OpenTelemetry GenAI semantic conventions have no stable release, and stabilizing them on top of fast-changing protocols is difficult. [13:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=780s)
- Container isolation is not secure enough for agents, and sandboxing remains an unsolved cat-and-mouse problem. [6:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=360s)
- SPIFFE/SPIRE gives fine-grained agent identity but has not become common because it is complex to deploy. [17:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=1020s)
- Getting started with agentic inference in production is much harder than with predictive inference, given GPU counts and redundancy. [29:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=1740s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| contribute | File issues on agent projects where trace context does not propagate correctly across A2A and MCP calls. | [24:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=1440s) |
| build | Put a credential-brokering proxy outside the agent sandbox so agents receive scoped capabilities instead of tokens. | [20:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=1200s) |
| build | Instrument agents from within using OpenTelemetry GenAI conventions and use the traces to drive eval loops. | [14:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=840s) |
| learn | Pick a pet project that uses agents, tracing and the inference stack (vLLM, llm-d, Ray) end to end. | [30:00](https://www.youtube.com/watch?v=oWFO88oAHOY&t=1800s) |

## Projects mentioned

[OpenTelemetry](https://github.com/open-telemetry/opentelemetry-collector), [Agent Sandbox](https://github.com/kubernetes-sigs/agent-sandbox), SPIFFE, SPIRE, Envoy AI Gateway, [llm-d](https://github.com/llm-d/llm-d), [vLLM](https://github.com/vllm-project/vllm), [Ray](https://github.com/ray-project/ray), Model Context Protocol
