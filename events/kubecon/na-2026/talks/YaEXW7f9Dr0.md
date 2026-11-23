# From Proxy to Platform: Building a Multi-Tenant AI Gateway

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Dibyo Mukherjee (Adobe), Tushar More (Adobe)  
**Video:** [YouTube](https://www.youtube.com/watch?v=YaEXW7f9Dr0) (22:12)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=From+Proxy+to+Platform%3A+Building+a+Multi-Tenant+AI+Gateway)  
**Tags:** `ai-gateway`, `multi-tenancy`, `platform-engineering`, `cost-governance`, `agents`

> Adobe built a shared, multi-tenant LLM gateway on LiteLLM, with its own control plane (console) for self-service model onboarding, fallbacks, budgets and logs. The talk walks through the stages from shared keys to team tenants, agent-driven usage and platform guarantees, and where they go next.

## Key points

- Before the gateway, teams shared long-lived provider keys or ran their own proxies, so nobody could say who used a key, what was spent per app, or whether proxies were patched. [3:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=180s)
- The data plane is LiteLLM, an OpenAI-compatible proxy with routing, fallbacks, auth, rate limits and budget checks; the team's work is the console control plane around it. [5:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=300s)
- When a second team arrived, each team got its own model deployments in its own cloud accounts, reachable only with team-scoped keys, so access and costs never mix. [6:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=360s)
- A tenant is a team, not a user, because use cases, service IDs and budgets belong to teams while people move between teams. Team admins self-serve models, fallback rules and budgets. [7:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=420s)
- Internal agents minted and deleted keys almost every turn, escaping key-based budgets. The fix: stamp the owning human on every key and reconcile agent spend back to that person's budget. [10:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=600s)
- For customer-facing agents, internal apps pass a customer ID via trusted headers or token claims, and the gateway enforces per-customer budgets and limits. A default budget is required, or customers get unlimited spend. [11:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=660s)
- Every request is attributed through tags minted into the key, so callers never send them per request. [11:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=660s)
- Platform guarantees: tested fallbacks on every upgrade, scaling on in-flight requests instead of CPU, and provider alerts that reach tenants rather than being swallowed. [12:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=720s)
- Upgrades flow dev, stage, prod via GitOps pull requests with a seven-day cooldown after a prod regression and API contract tests; CVE fixes skip the cooldown and ship the same day. [13:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=780s)
- On Kubernetes: isolated namespaces with network policies, no keys in pods, tenant IAM roles, KEDA scaling on in-flight requests, PodDisruptionBudgets, long drain grace periods, Argo CD sync and rollback, and one Helm chart per region. [15:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=900s)
- Next: multi-region with full in-region stacks for data residency, tenant-defined auto routing with evals to check cost/quality, and moving from keys to agent and workload identity. [17:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=1020s)

## Numbers stated

- Seven-day cooldown between dev and prod promotion for new LiteLLM versions. [14:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=840s)
- The infrastructure team runs hundreds of clusters across clouds. [1:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=60s)

## Open gaps

- Data residency requires running the whole stack in one region, and not every provider offers every model in every region, so fallback config must also be region-bound. Still in design. [17:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=1020s)
- Keys still carry budgets and attribution; replacing them with agent identity tied to internal identity systems or Kubernetes service accounts is longer term. [18:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=1080s)
- Auto routing is only in pilot; tenants need a way to prove it gives the cost/quality tradeoff they want. [17:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=1020s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Stamp an owning human or customer ID on every gateway key and enforce default budgets so agent-minted keys cannot bypass limits. | [10:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=600s) |
| build | Autoscale LLM proxies on in-flight requests with KEDA instead of CPU. | [15:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=900s) |
| learn | Add API contract tests and a cooldown stage to your gateway upgrade pipeline, with a fast path for CVE fixes. | [14:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=840s) |
| write | Describe a maturity model for your own AI gateway using the stages here: shared keys, team tenants, agents, platform guarantees. | [18:00](https://www.youtube.com/watch?v=YaEXW7f9Dr0&t=1080s) |

## Projects mentioned

LiteLLM, [Kubernetes](https://github.com/kubernetes/kubernetes), [KEDA](https://github.com/kedacore/keda), Argo CD, Envoy, [agentgateway](https://github.com/agentgateway/agentgateway), Cluster API, Helm
