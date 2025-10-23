# Topology

## Core

In the context of a distributed system, **topology** refers to the arrangement of the nodes and the communication links between them. The network topology has a significant impact on the performance, reliability, and scalability of the system.

Different topologies have different characteristics. For example, some topologies are more fault-tolerant than others, while some are more scalable. The choice of which topology to use depends on the specific requirements of the application.


### Key Considerations

-   **Fault Tolerance:** The ability of the topology to withstand node or link failures without disrupting the entire system.
-   **Scalability:** How easily new nodes can be added to the network without significant redesign or performance degradation.
-   **Cost:** The financial expense associated with cabling, hardware, and maintenance for a given topology.
-   **Performance:** The impact of the topology on communication latency and bandwidth.
-   **Complexity:** The ease or difficulty of implementing, managing, and troubleshooting the network.
-   **Security:** How the topology affects the network's vulnerability to attacks and unauthorized access.

## Comparison

| Topology | Reliability | Scalability | Cost | Use Case |
|---|---|---|---|---|
| **[Bus](./bus)** | Low | Low | Low | Small networks |
| **[Star](./star)** | Medium | Low | Medium | Local area networks (LANs) |
| **[Ring](./ring)** | High | Low | Medium | Telecom networks |
| **[Mesh](./mesh)** | High | High | High | Wide area networks (WANs) |
| **[Tree](./tree)** | Medium | High | High | Large networks |
