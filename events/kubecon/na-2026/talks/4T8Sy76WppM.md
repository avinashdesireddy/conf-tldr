# Least-Privilege by Default: Standardizing Identity-Aware AI Agent Access into a Golden Path

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Masato Kozuka (Hitachi, Ltd.)  
**Video:** [YouTube](https://www.youtube.com/watch?v=4T8Sy76WppM) (33:56)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Least-Privilege+by+Default%3A+Standardizing+Identity-Aware+AI+Agent+Access+into+a+Golden+Path)  
**Tags:** `agent-security`, `identity`, `platform-engineering`, `golden-path`, `mcp`

> Least privilege for an agent acting on a user's behalf means every call may do only what both the user and the agent are allowed to do. Hitachi's design builds seven rules into a platform golden path using Keycloak token exchange, SPIFFE/SPIRE attestation, attribute-based policy and Backstage templates, so teams only declare and approve.

## Key points

- MCP made connecting tools easy, but each team secures access its own way (agent's own account, static keys, homemade token checks), causing both vulnerabilities and platform sprawl. [1:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=60s)
- Pillar 1, on whose behalf: keep the user in the sub claim at every hop by exchanging the token for a new one with the next server as audience, instead of passing the first token along. [4:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=240s)
- The common shortcut, client credentials, makes the agent act as itself (a confused deputy); disable agent service accounts in the authorization server and reject tokens without a user at the MCP server. [5:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=300s)
- Pillar 2, which agent: SPIFFE attests the pod (namespace, image digest) and issues a short-lived ID; the authorization server accepts only that, not static client secrets, and writes the agent into the client_id claim. [7:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=420s)
- Pillar 3, what is allowed: the authorization server issues tokens only for approved targets, and the MCP server runs a policy check on both user and agent attributes, e.g. low agent clearance blocks a high-sensitivity payment tool. [10:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=600s)
- A server that skips the audience check accepts tokens meant for another server and defeats target restriction; one team's leaked key can then reach another team's server. [11:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=660s)
- Delivery: three rules live in the authorization server (Keycloak with SPIRE), four in the agent sidecar and server middleware shipped via Backstage templates; teams write only their tools. [13:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=780s)
- Each agent's client is generated from its declaration, not set by hand, because a misconfigured target in the shared layer would affect every agent. [16:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=960s)
- Broad declarations are split into one request per target, each approved by that server's owner, so approval does not pile up in a central team. [19:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=1140s)
- Demo: a receipt with a hidden instruction to fetch payroll data fails because Keycloak never issues a payroll token for the expense agent. [23:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=1380s)
- Q&A: for SaaS products that do not accept these tokens, an ingress gateway can run the same policy in front of them. [28:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=1680s)

## Numbers stated

- Seven rules across three pillars. [12:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=720s)

## Open gaps

- Agents with no user behind them are out of scope for this model. [3:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=180s)
- A team can still build a server by hand without the template and skip the audience check. [17:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=1020s)
- User identity cannot be propagated into SaaS products that accept only API keys, so their audit logs show a service account. [29:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=1740s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Ship MCP server and agent templates with token exchange, audience checks, user-required checks and attribute-based policy built in. | [17:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=1020s) |
| build | Replace static agent keys with SPIRE-attested workload identity accepted by your authorization server. | [8:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=480s) |
| build | Add a declare-and-approve flow where each target server's owner approves agent access and the platform generates the client. | [20:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=1200s) |
| learn | OAuth 2.0 Token Exchange and the confused deputy problem for agents acting on behalf of users. | [5:00](https://www.youtube.com/watch?v=4T8Sy76WppM&t=300s) |

## Projects mentioned

Keycloak, SPIFFE, SPIRE, Backstage, MCP, [Kubernetes](https://github.com/kubernetes/kubernetes)
