# From Laptop to Cluster: The Agentic AI Inner Loop on Kubernetes

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Kevin Dubois (IBM)  
**Video:** [YouTube](https://www.youtube.com/watch?v=KCBdIFOmzEU) (30:22)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=From+Laptop+to+Cluster%3A+The+Agentic+AI+Inner+Loop+on+Kubernetes)  
**Tags:** `agents`, `developer-experience`, `mcp`, `a2a`, `java`

> Using a live audience race game run by an AI race director, the speaker shows an agentic Java app built with Quarkus and LangChain4j that exposes MCP tools and calls sub-agents over A2A. He argues agents are mostly ordinary code: develop locally with hot reload and a dev UI, add evals, then ship to Kubernetes with configuration changes and standard security and health patterns.

## Key points

- Gartner research cited: many agentic AI projects will be canceled because of rising costs, unclear business value and weak risk controls. [1:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=60s)
- The demo game sends phone taps through Kafka to a dashboard, with an AI race director that monitors the race, changes themes and boosts teams that fall behind, with human approval. [4:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=240s)
- The game exposes MCP servers; the admin server requires browser authentication so not every user or agent can control the game. [6:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=360s)
- The race director is a supervisor agent that picks between an analyst and a creative sub-agent over A2A, similar to distributed services owned by different teams. [10:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=600s)
- MCP and A2A act like a new REST: MCP tools are annotated Java methods with role-based access, such as admin-only tools. [11:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=660s)
- An open-source tool can turn existing APIs into MCP servers by configuration, without rewriting them. [13:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=780s)
- Quarkus dev mode gives hot reload, a dev UI listing Kafka topics, AI services, MCP tools, prompt templates and token metrics, and exposes runtime info to the code assistant over MCP. [16:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=960s)
- Local development still enforces the same MCP authentication, so you test production auth on your laptop. [20:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=1200s)
- Swapping models changes behavior: a boost prompt produced a 1.5 multiplier on one model and 3 on another, so add evals to the test suite. [24:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=1440s)
- For production: switch models via configuration, add health checks for sub-agents and MCP servers, expose token and latency metrics, use mutual TLS and short-lived tokens (SPIFFE/SPIRE, Keycloak). [26:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=1560s)

## Numbers stated

- Gartner expects more than 40% of agentic AI projects to be canceled by the end of next year. [1:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=60s)
- The same boost prompt gave a 1.5 multiplier on the original model and 3 on a new one. [24:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=1440s)
- Local load test simulated 100 players. [20:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=1200s)

## Open gaps

- Agentic apps with many components are hard to test, and a race director and code assistant can conflict over the same controls. [9:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=540s)
- Changing models can silently change agent behavior unless prompts are detailed and evals cover it. [24:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=1440s)
- Agents need guardrails, sandboxing and least-privilege, short-lived credentials when they run in Kubernetes. [2:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=120s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Add evals for non-deterministic agent behavior to your test suite with tools like Langfuse or Promptfoo. | [25:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=1500s) |
| build | Add health endpoints that check A2A sub-agents and MCP servers, not just the main app. | [26:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=1560s) |
| learn | Try the game's source on GitHub to see MCP tools with role-based access and an A2A supervisor agent in Java. | [28:00](https://www.youtube.com/watch?v=KCBdIFOmzEU&t=1680s) |
| contribute | Join the CNCF developer experience TAG, which the speaker says is looking for contributors. | [0:00](https://www.youtube.com/watch?v=KCBdIFOmzEU) |

## Projects mentioned

Quarkus, LangChain4j, Model Context Protocol, A2A, Apache Kafka, [Prometheus](https://github.com/prometheus/prometheus), Langfuse, Promptfoo, SPIFFE/SPIRE, Keycloak, Argo Rollouts, [Kubernetes](https://github.com/kubernetes/kubernetes)
