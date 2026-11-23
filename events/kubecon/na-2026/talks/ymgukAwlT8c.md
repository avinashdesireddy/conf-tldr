# Who Ran Up the Inference Bill? AI Traffic Control with KServe and Gateway API Inference Extensions

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Lasse Vierow (Independent)  
**Video:** [YouTube](https://www.youtube.com/watch?v=ymgukAwlT8c) (15:52)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Who+Ran+Up+the+Inference+Bill%3F+AI+Traffic+Control+with+KServe+and+Gateway+API+Inference+Extensions)  
**Tags:** `ai-inference`, `ai-gateway`, `cost`, `rate-limiting`, `gateway-api`

> A beginner-level talk on attributing and controlling inference spend by putting an AI-aware gateway in front of KServe models. A live demo on kind uses agentgateway with the Gateway API Inference Extension to log tokens per team, enforce per-team token budgets, block sensitive data and fail over to a cloud LLM.

## Key points

- Inference bills show a total but not which team or service spent the tokens, and request counts mislead because token use per request varies widely. [2:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=120s)
- Inference traffic differs from classic traffic: seconds to minutes, streamed token by token, costly, routed on the body, so request limits and round-robin balancing stop working. [3:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=180s)
- KServe creates the HTTPRoute, InferencePool and endpoint picker from one model resource. [4:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=240s)
- The endpoint picker chooses pods using KV cache, prefix and LoRA adapter state instead of load alone. [6:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=360s)
- Any gateway that supports the Inference Extension works; the demo uses agentgateway as the AI-aware gateway. [6:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=360s)
- Local models need a cost too; a rough GPU-hours-over-tokens figure is enough to visualize spend. [7:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=420s)
- Plain Gateway API logs show only status codes; with the inference extension, logs include input and output tokens and the model. [10:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=600s)
- Per-team traffic showed the team with the fewest requests spent the most tokens. [12:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=720s)
- A guardrail rejected a prompt containing a credit card number at the gateway; a team past its token budget got 429s while other teams kept working. [12:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=720s)
- When the local model returned 500, the gateway failed over to a cloud LLM without interrupting users. [14:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=840s)
- Takeaways: meter tokens not requests, put a name on every token, control spend at the gateway, build on standards and keep policy thin. [14:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=840s)

## Numbers stated

- Example per-team budget: 60,000 tokens, after which requests get HTTP 429. [13:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=780s)
- Mock LLM log entry: 6 input tokens, 1 output token. [11:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=660s)
- The ML research team sent only 3 requests but spent the most tokens. [12:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=720s)

## Open gaps

- Per-token cost for self-hosted models is a rough estimate, not a production calculation. [7:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=420s)
- Classic request limits and round-robin load balancing do not fit token-based inference traffic. [3:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=180s)
- Standard Gateway API logs carry no token or model data without an inference-aware gateway. [10:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=600s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| build | Add per-team token budgets and failover to a cloud model at your AI gateway. | [13:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=780s) |
| learn | Run the speaker's kind-based demo repo with KServe and agentgateway. | [9:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=540s) |
| build | Export gateway token logs to your monitoring stack to split the inference bill by team. | [11:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=660s) |
| contribute | Join the KServe CNCF Slack or the agentgateway Discord to work on AI gateway features. | [15:00](https://www.youtube.com/watch?v=ymgukAwlT8c&t=900s) |

## Projects mentioned

[KServe](https://github.com/kserve/kserve), [Gateway API](https://github.com/kubernetes-sigs/gateway-api), [Gateway API Inference Extension](https://github.com/kubernetes-sigs/gateway-api-inference-extension), [agentgateway](https://github.com/agentgateway/agentgateway), kind, cert-manager, [Kubernetes](https://github.com/kubernetes/kubernetes)
