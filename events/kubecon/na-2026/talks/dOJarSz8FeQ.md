# Agentic AI: Let’s Build a Reference Architecture, Live? Or at Least Try!

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Ricardo Rocha (CERN)  
**Video:** [YouTube](https://www.youtube.com/watch?v=dOJarSz8FeQ) (33:11)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Agentic+AI%3A+Let%E2%80%99s+Build+a+Reference+Architecture%2C+Live%3F+Or+at+Least+Try%21)  
**Tags:** `agents`, `reference-architecture`, `end-users`, `agent-security`, `community`

> In a CNCF End User Technical Advisory Board session, Ricardo Rocha drew a layered agentic AI reference architecture live from audience input: gateway, orchestration, sandboxing, inference, infrastructure and observability. Attendees named their tools and gaps, mainly caller identity, data privacy and the lack of a shared agent harness, and were asked to submit their own reference architectures.

## Key points

- The End User TAB publishes end-user reference architectures at endusers.cncf.io: projects used, diagrams, what worked, what did not, and what glue had to be built. [2:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=120s)
- Audience-proposed layers: gateway, data sources, inference, policies, network policies, and agent frameworks such as LangChain. [5:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=300s)
- Identity: one attendee sees caller identity lost as requests move toward the model and wants it carried end to end, for example with SPIFFE/SPIRE or signing. [10:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=600s)
- Another attendee, on AWS only, assumes a role through an IdP and SigV4-signs every request through the pipeline. [11:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=660s)
- Privacy: one team tokenizes and anonymizes sensitive fields before they reach a model and reverses it on the response. [13:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=780s)
- Gateway tools named: Envoy, agentgateway (split into MCP and LLM roles) and LiteLLM, used in front of Bedrock for routing, team access and quotas. [14:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=840s)
- Egress control: per-agent allowlists of DNS names so each agent reaches only the domains its tools need. [18:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=1080s)
- One attendee embeds the harness in each web app to reuse the user's session and permissions, but gets no shared observability. [20:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=1200s)
- Some workloads are tens of thousands of one-shot agents that never resume, unlike long-running coding agents, which changes how useful pause and resume is. [22:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=1320s)
- Sandboxes named: Kata Containers, gVisor, Bubblewrap and Firecracker. Inference: NVIDIA Dynamo, Triton, vLLM, Ollama, SGLang and llama.cpp. Agent observability: Langfuse. [23:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=1380s)
- Multiple submissions in one area would let the TAB build a domain-level reference architecture from common patterns. [29:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=1740s)

## Numbers stated

- Show of hands: about five deploy only in public cloud, one only on premises, the rest mixed. [26:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=1560s)
- One use case has tens of thousands of agents with one to three turns each. [22:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=1320s)
- Example egress allowlist: about 10 domains per agent. [18:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=1080s)

## Open gaps

- Caller identity is often lost between the agent layer and the inference engine, so requests cannot be attributed. [12:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=720s)
- Privacy handling for data sent to third-party inference gets little attention at the conference. [13:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=780s)
- No shared harness pattern: teams re-implement the harness per application, without common observability. [20:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=1200s)
- There is no stable reference architecture yet; teams are early and still iterating. [4:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=240s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| write | Submit your agent platform as a CNCF end-user reference architecture, including what did not work and the glue you built. | [28:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=1680s) |
| build | Build a tokenization step that strips sensitive fields before inference and restores them in the response. | [14:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=840s) |
| build | Enforce per-agent FQDN egress allowlists for agent workloads. | [18:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=1080s) |
| contribute | Join the End User TAB meetings or a domain user group to share agentic AI deployment feedback. | [30:00](https://www.youtube.com/watch?v=dOJarSz8FeQ&t=1800s) |

## Projects mentioned

Envoy, [agentgateway](https://github.com/agentgateway/agentgateway), LiteLLM, LangChain, Langfuse, n8n, SPIFFE, SPIRE, [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-collector), [Prometheus](https://github.com/prometheus/prometheus), Kata Containers, [gVisor](https://github.com/gvisor/gvisor), Bubblewrap, Firecracker, [NVIDIA Dynamo](https://github.com/ai-dynamo/dynamo), [Triton Inference Server](https://github.com/triton-inference-server/server), [vLLM](https://github.com/vllm-project/vllm), Ollama, [SGLang](https://github.com/sgl-project/sglang), llama.cpp, Amazon Bedrock
