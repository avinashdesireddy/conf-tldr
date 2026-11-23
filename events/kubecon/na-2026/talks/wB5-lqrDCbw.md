# Governing and Scaling Agents in Heterogeneous Environments

**Event:** KubeCon + CloudNativeCon North America 2026 · Track not yet assigned  
**Speakers:** Antonio Ojea (Google), Tomás Tormo (Nearform Ltd)  
**Video:** [YouTube](https://www.youtube.com/watch?v=wB5-lqrDCbw) (31:33)  
**Slides:** [Find slides on Sched](https://kccncna2026.sched.com/search?q=Governing+and+Scaling+Agents+in+Heterogeneous+Environments)  
**Tags:** `agent-security`, `agent-networking`, `zero-trust`, `peer-to-peer`, `policy`

> Antonio Ojea and Tomás Tormo present Agent Mesh, a network for agents running on Kubernetes, laptops, VMs and serverless, built on a libp2p peer-to-peer data plane with Kademlia discovery. Policy travels with each node as signed, attenuable Biscuit tokens minted at enrollment, and a live hospital demo shows label-based rules keeping EU data in the EU.

## Key points

- Regulated customers run agents on laptops, VMs and serverless as well as Kubernetes, and cannot replace existing platforms, so a Kubernetes-only answer creates silos. [3:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=180s)
- The solution must run as an SDK, a sidecar or a gateway and work with existing open protocols. [4:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=240s)
- A VPN does not fit: it gives L3/L4 connectivity with IPAM pain and no visibility, and a compromised agent gets open access. [6:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=360s)
- Agent traffic falls into five kinds: LLM calls, tools over MCP, agent-to-agent (A2A), external apps such as GitHub, and services the agent exposes. [6:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=360s)
- Data plane: libp2p over a Kademlia DHT, with a cryptographic identity per node, TLS between nodes and built-in service discovery. [9:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=540s)
- Policy: webhooks and Lua/Wasm extensions are opaque and fragile, so they chose Biscuit, signed tokens with a Datalog policy language, exposed to admins through a simpler DSL. [11:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=660s)
- The control plane connects to an external identity provider, compiles policy to Datalog and mints a Biscuit at enrollment. Biscuits work offline, so connected nodes no longer need the control plane. [14:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=840s)
- Biscuit blocks can only attenuate, so a node can narrow delegated rights, for example to one MCP tool or one HTTP path. [15:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=900s)
- Nodes set label requirements for inbound and outbound peers (for example region EU), checked in a five-step exchange before any data flows. [16:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=960s)
- Architecture: control plane, admin-run routers that keep the Kademlia network up, and nodes or embedded SDKs; one binary bundles control plane, router and console. [18:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=1080s)
- Demo: the US diagnoser is refused by the laptop's EU-only egress rule, and the model cannot override it because the node enforces it; a banned phone is cut off after the control plane notifies peers. [23:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=1380s)

## Numbers stated

- A new mesh can be created in about 10 seconds using a tunnel broker. [19:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=1140s)
- Five categories of agent traffic: LLM, MCP tools, A2A, external apps, exposed services. [6:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=360s)
- A five-step check runs between nodes before any data flows. [17:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=1020s)
- Agent Mesh v0.2.0 was just released. [30:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=1800s)

## Open gaps

- Schema-based filtering of MCP traffic is hard to maintain when there can be millions of tools and fields change often. [10:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=600s)
- Region rules depend on admins labeling nodes correctly; the mesh only enforces the labels it is given. [17:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=1020s)
- Next: connecting HPC centers and cloud providers to run workflows, with Lawrence Livermore National Lab, and closer work with the A2A protocol. [30:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=1800s)

## Opportunities

| Type | Opportunity | At |
|---|---|---|
| learn | Biscuit tokens: offline verification, Datalog policies and attenuation for delegating narrower rights to sub-agents. | [12:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=720s) |
| build | Enforce data residency for agent traffic with signed node labels and egress requirements instead of prompt instructions. | [23:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=1380s) |
| learn | Create a mesh or join the public testnet and connect agents across a laptop, a VM and a cluster. | [31:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=1860s) |
| contribute | Help with Agent Mesh's A2A integration or new SDK and platform integrations. | [30:00](https://www.youtube.com/watch?v=wB5-lqrDCbw&t=1800s) |

## Projects mentioned

Agent Mesh, libp2p, Kademlia, Biscuit, CEL, MCP, A2A, Envoy, [Istio](https://github.com/istio/istio), [Kubernetes](https://github.com/kubernetes/kubernetes), Agent Substrate, Cloud Run, Gemini, Claude
