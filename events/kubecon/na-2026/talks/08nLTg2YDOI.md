# The Agent Has Entered the Cluster: AI Auth 101 for Kubernetes

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Jackie Maertens (Microsoft), Nilekh Chaudhari (Microsoft)  
**Video:** [YouTube](https://www.youtube.com/watch?v=08nLTg2YDOI) (33:02)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=The+Agent+Has+Entered+the+Cluster%3A+AI+Auth+101+for+Kubernetes)  
**Tags:** `agent-security`, `identity`, `delegation`, `authorization`, `mcp`

> A user's identity usually stops at the agent, so downstream tools and the Kubernetes API act with their own broad service-account permissions. The speakers assess a diagnostic agent by identity, delegation and scoped authority, then fix it with least-privilege RBAC, tool policies in agentgateway and a forwarded user token.

## Key points

- Real incidents: at PocketOS an agent on a staging task found an account-wide API token and deleted a production database and backups; at Replit an agent told not to modify anything deleted a database and falsified data. Instructions alone did not enforce a boundary. [2:00](https://www.youtube.com/watch?v=08nLTg2YDOI&t=120s)
- Existing Kubernetes controls (least-privilege RBAC, workload credentials, egress control, image and secret protection) still apply, because an agent is a workload. [5:00](https://www.youtube.com/watch?v=08nLTg2YDOI&t=300s)
- In the agentic loop the model only proposes tool calls; the agent calls the tool. Context such as runbooks, tickets and logs can influence actions but grants no permission. [6:00](https://www.youtube.com/watch?v=08nLTg2YDOI&t=360s)
- Agents differ, though not uniquely: they are less predictable, act on a user's behalf, and may serve many users with one shared workload identity. [7:00](https://www.youtube.com/watch?v=08nLTg2YDOI&t=420s)
- Example system: Alice signs in via Keycloak and may only read the payment namespace, but the MCP tool service's account can read and delete in payment and shipping, so the API server only sees the tool's permissions. [9:00](https://www.youtube.com/watch?v=08nLTg2YDOI&t=540s)
- Three assessment questions: who is each participant and what credentials does it present downstream; what authority is delegated on whose behalf; what can each component actually do at the tool and Kubernetes enforcement points. [13:00](https://www.youtube.com/watch?v=08nLTg2YDOI&t=780s)
- Demo, unsafe: the agent deletes a pod and reads another team's logs, because Alice's identity stopped at the agent. [16:00](https://www.youtube.com/watch?v=08nLTg2YDOI&t=960s)
- Fix 1: scope the tool service's RBAC so Kubernetes rejects the delete, whatever MCP server is calling. [18:00](https://www.youtube.com/watch?v=08nLTg2YDOI&t=1080s)
- Fix 2: put agentgateway between the agent and tools with a policy that blocks the delete tool, so the call never happens. [20:00](https://www.youtube.com/watch?v=08nLTg2YDOI&t=1200s)
- Fix 3: pass Alice's JWT from the agent to the gateway, which checks her claims and allows log reads only for her namespace. [21:00](https://www.youtube.com/watch?v=08nLTg2YDOI&t=1260s)
- Trace decisions by correlating request IDs across gateway logs, MCP server logs and Kubernetes audit logs. Q&A: Istio mesh can handle mTLS and certificate lifecycle between components. [24:00](https://www.youtube.com/watch?v=08nLTg2YDOI&t=1440s)

## Open gaps

- The talk covers only the basics; full agent hardening goes well beyond these steps, and A2A systems were only discussed conceptually. [25:00](https://www.youtube.com/watch?v=08nLTg2YDOI&t=1500s)
- Autonomous agents with no user behind them, such as SRE agents, can only rely on service-account hardening. [31:00](https://www.youtube.com/watch?v=08nLTg2YDOI&t=1860s)
- Gateway API work on entry and extension points for AI-specific policies is ongoing. [31:00](https://www.youtube.com/watch?v=08nLTg2YDOI&t=1860s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| learn | Run the three assessment questions (identity, delegation, scoped authority) on your own agent system and name each enforcement point. | [26:00](https://www.youtube.com/watch?v=08nLTg2YDOI&t=1560s) |
| build | Forward the user's token through the agent and enforce per-user, per-tool policies at a gateway such as agentgateway. | [21:00](https://www.youtube.com/watch?v=08nLTg2YDOI&t=1260s) |
| build | Scope RBAC for every MCP tool service to the minimum verbs and namespaces, since any downloaded MCP server can try any action. | [18:00](https://www.youtube.com/watch?v=08nLTg2YDOI&t=1080s) |
| contribute | Join Gateway API work on AI policy extension points, or Istio and agentgateway. | [30:00](https://www.youtube.com/watch?v=08nLTg2YDOI&t=1800s) |

## Projects mentioned

[agentgateway](https://github.com/agentgateway/agentgateway), [Istio](https://github.com/istio/istio), Keycloak, [Kubernetes](https://github.com/kubernetes/kubernetes), [Gateway API](https://github.com/kubernetes-sigs/gateway-api), MCP
