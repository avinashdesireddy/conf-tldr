# Just Keep Swimming: Benchmarking OSS Agent Memory on Kubernetes with OpenTelemetry

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Henrik Rexed (Dynatrace)  
**Video:** [YouTube](https://www.youtube.com/watch?v=LSFk3nqozcY) (31:29)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Just+Keep+Swimming%3A+Benchmarking+OSS+Agent+Memory+on+Kubernetes+with+OpenTelemetry)  
**Tags:** `agents`, `agent-memory`, `benchmarking`, `observability`, `kagent`

> Henrik Rexed benchmarks five open-source agent memory servers on kagent with a shared generic MCP layer and OpenTelemetry instrumentation he contributed upstream. Memory helps only when recall is precise: embedding and graph approaches did best for SRE investigations, a key-based store did best for context-rich coding crews, and MemPalace and Zep were the most consistent overall.

## Key points

- Agents without memory repeat investigations and tool calls they already did, wasting tools and tokens; memory servers let agents store and recall facts. [2:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=120s)
- Architectures range from pure embeddings, to vector plus graph, knowledge graphs, temporal knowledge graphs, and a key/metadata store plus vector and graph (MemKeys, the speaker's own two-week-old project). [4:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=240s)
- Common layers: ingest and search paths, an optional LLM to embed and categorize facts, graph building done asynchronously, and usually an MCP server for agent access. [5:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=300s)
- MemPalace organizes memory into wings per project and drawers per category; Zep (Graphiti) tracks when facts change so it can answer what was true before and now. [7:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=420s)
- Harness: kagent agents on DeepSeek, a generic MCP for add, search, get, update and delete so only the backend changes, and OpenTelemetry instrumentation contributed to each backend (some PRs were rejected, so forks were used). [11:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=660s)
- Scenario 1: an SRE agent diagnoses Kubernetes failures (CrashLoopBackOff, ImagePullBackOff, OOM kills, pending pods) and bad Gateway API and GAMMA gRPC route configs, measured as warm minus cold runs. [14:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=840s)
- Scenario 2: a BMAD-method crew over A2A builds an expense approval app, is stopped mid-feature and resumed, then gets a fact change (PostgreSQL to MySQL). [15:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=900s)
- Memory raises input tokens, though these may be billed as cached input; retrieving too many or wrong facts confuses the LLM and makes results worse. [18:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=1080s)
- SRE results: MemOS, Zep and MemPalace improved with memory; Mem0 and MemKeys got worse, with MemKeys pulling far too many facts. [19:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=1140s)
- Coding crew results: the key store did best on build, resume and restart, using far fewer tokens because tasks carry rich context; MemPalace and Zep also did well. [20:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=1200s)
- Few backends offer a UI to inspect stored memory, which matters for pruning noise that degrades search. [26:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=1560s)

## Numbers stated

- Memory server footprint was around 250 to 300 MB. [18:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=1080s)
- MemKeys used about 55 millicores of CPU on retrieval in the SRE scenario. [18:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=1080s)
- In the coding scenario MemKeys used about 20 millicores more than the others. [21:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=1260s)
- Add and search latencies were on the scale of a few microseconds, up to about 20 microseconds. [22:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=1320s)
- The other projects have more than 10K GitHub stars; MemKeys has zero. [23:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=1380s)

## Open gaps

- Most memory backends do not ship OpenTelemetry support, and some maintainers rejected upstream PRs because telemetry is a commercial feature. [13:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=780s)
- Memory scoping and isolation between users or channels was not evaluated, and the speaker did not know which backends support it. [27:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=1620s)
- Several earlier candidates (Cognee, Memu, Honcho) were dropped over licensing changes, and other popular tools are not yet covered. [29:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=1740s)
- Adding a backend to the benchmark is laborious: MCP connectivity, OpenTelemetry instrumentation, then scenario design. [30:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=1800s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| contribute | Add OpenTelemetry instrumentation for ingest and recall operations to open-source memory servers. | [13:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=780s) |
| build | Measure agent memory as warm-run minus cold-run tokens and tool calls on your own workloads before adopting a backend. | [14:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=840s) |
| build | Test whether memory backends isolate recall by user or channel before using them in shared bots. | [27:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=1620s) |
| learn | Compare embedding, temporal knowledge graph and key-indexed memory designs against SRE-style versus project-style agent tasks. | [22:00](https://www.youtube.com/watch?v=LSFk3nqozcY&t=1320s) |

## Projects mentioned

kagent, [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-collector), Mem0, MemOS, MemPalace, Zep, Graphiti, MemKeys, Neo4j, BMAD Method, [Gateway API](https://github.com/kubernetes-sigs/gateway-api), Model Context Protocol, A2A, DeepSeek
