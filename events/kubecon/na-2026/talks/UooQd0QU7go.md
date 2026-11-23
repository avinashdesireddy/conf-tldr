# Simulate, Evolve, Validate, Ship: AI-Discovered Algorithms for LLM Serving Stacks

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Jing Chen (IBM), Mert Toslali (IBM)  
**Video:** [YouTube](https://www.youtube.com/watch?v=UooQd0QU7go) (28:43)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Simulate%2C+Evolve%2C+Validate%2C+Ship%3A+AI-Discovered+Algorithms+for+LLM+Serving+Stacks)  
**Tags:** `ai-inference`, `agents`, `simulation`, `admission-control`, `llm-d`

> IBM Research uses a CPU-based simulator of llm-d and vLLM plus an agentic harness to discover serving policies, then validates the winners on GPUs and upstreams them to llm-d. The loop has produced admission control, flow control and LoRA routing plugins for the llm-d router.

## Key points

- Every llm-d subsystem (routing, admission control, flow control, scheduling, prefill/decode, autoscaling) is an open design problem, but GPU experiments take days and cost thousands of dollars, so few ideas get tested. [1:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=60s)
- The loop is simulate, evolve, validate, ship. A human gives only the goal, SLO constraints, workloads and hardware; the output is a production-ready llm-d policy. [2:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=120s)
- The simulator (BLIS) is a digital twin of llm-d and vLLM that runs on CPUs. An agentic harness plans hypotheses, writes algorithms as code, runs them in the simulator and learns across iterations. [3:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=180s)
- Simulation confirms the direction of a gain; real hardware measures its size. Validation turns simulated code and config into llm-d code, deploys it and benchmarks it. [6:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=360s)
- Translation uses three agents: one maps signals between simulator and llm-d (KV cache utilization, queue depth, priority), a writer translates, and a reviewer tests. Agents check each other's work, not their own. [7:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=420s)
- A time-unit mismatch in saturation detection between simulator and llm-d invalidated hours of GPU results. They added pre-deploy parity checks and post-benchmark log checks. [8:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=480s)
- Attaching real benchmark evidence to PRs made upstream review faster. Three policies were merged into the llm-d router: admission gate, flow control and LoRA routing. [10:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=600s)
- The baseline admission gate accepts everything until saturation hits 100%, when queues are already long. The new probabilistic admitter rejects low-priority requests with probability rising with saturation and always accepts critical ones. [13:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=780s)
- The soft reflective ceiling flow-control policy orders admitted requests so critical traffic is never blocked behind low-priority work, slowing low-priority queues as load rises without rejecting anything. [17:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=1020s)
- Both are llm-d plugins enabled with a configuration change. [19:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=1140s)
- Q&A: a prompted agent with a methodology file forgot to persist algorithms and workloads and made false claims, so they built a harness with deterministic tooling and hypothesis bundles (main, negative, ablation arms). [22:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=1320s)

## Numbers stated

- The simulator runs about 200x faster than real GPU inference. [3:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=180s)
- Validation setup: four H100 GPUs, a Qwen 14B model, eight workloads across four shapes (chatbot, code generation, agentic and others) at various loads. [15:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=900s)
- Probabilistic admission: critical-request TTFT improved by up to 97% and end-to-end latency by up to 50%, at the cost of more low-priority rejections. [15:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=900s)
- Flow-control policy: critical TTFT improved by up to 98%, latency improved by up to 50x, with zero requests rejected. [18:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=1080s)

## Open gaps

- Running the loop continuously against live traffic is the goal but not reached; every step can fail and still needs human review of logs. [27:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=1620s)
- llm-d, the simulator and the harness all keep changing, which makes unattended overnight discovery hard. [27:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=1620s)
- Sim-to-real translation is error prone; one config mismatch forced discarding a full GPU run. [9:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=540s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| learn | Enable the new admission and flow-control plugins in llm-d and compare critical-request TTFT with the baseline under overload. | [19:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=1140s) |
| build | Use a CPU simulator to screen scheduling or admission policies against SLOs before spending GPU time. | [3:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=180s) |
| build | Give coding agents deterministic tooling that forces them to persist algorithms, workloads and results before claiming success. | [22:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=1320s) |
| contribute | Attach simulation and real-cluster benchmark evidence to llm-d PRs that change routing or scheduling policies. | [10:00](https://www.youtube.com/watch?v=UooQd0QU7go&t=600s) |

## Projects mentioned

[llm-d](https://github.com/llm-d/llm-d), [vLLM](https://github.com/vllm-project/vllm), BLIS
