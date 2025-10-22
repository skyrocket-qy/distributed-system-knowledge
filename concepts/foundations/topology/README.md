# Topology

## Core

In the context of a distributed system, **topology** refers to the arrangement of the nodes and the communication links between them. The network topology has a significant impact on the performance, reliability, and scalability of the system.

Different topologies have different characteristics. For example, some topologies are more fault-tolerant than others, while some are more scalable. The choice of which topology to use depends on the specific requirements of the application.

### Common Network Topologies

There are a number of different network topologies that can be used in a distributed system. Some of the most common ones include:

- **Bus:** All nodes are connected to a single, shared communication link. This is a simple topology, but it has a single point of failure.
- **Star:** All nodes are connected to a central hub. This is a more fault-tolerant topology than the bus, but the hub can become a bottleneck.
- **Ring:** All nodes are connected in a closed loop. This is a simple and reliable topology, but it can be difficult to add and remove nodes.
- **Mesh:** All nodes are connected to all other nodes. This is the most fault-tolerant topology, but it is also the most expensive to build and maintain.
- **Tree:** A hybrid topology that combines the bus and star topologies. This is a scalable and flexible topology, but it can be complex to manage.

The choice of which topology to use is a trade-off between a number of factors, including cost, performance, reliability, and scalability.

### Key Considerations

-   **Fault Tolerance:** The ability of the topology to withstand node or link failures without disrupting the entire system.
-   **Scalability:** How easily new nodes can be added to the network without significant redesign or performance degradation.
-   **Cost:** The financial expense associated with cabling, hardware, and maintenance for a given topology.
-   **Performance:** The impact of the topology on communication latency and bandwidth.
-   **Complexity:** The ease or difficulty of implementing, managing, and troubleshooting the network.
-   **Security:** How the topology affects the network's vulnerability to attacks and unauthorized access.

## Characteristics

- **Reliability**: The ability of a topology to withstand failures.
- **Scalability**: The ability of a topology to grow as the number of nodes increases.
- **Cost**: The cost of implementing and maintaining a topology.
- **Performance**: The performance of a topology in terms of latency and bandwidth.
- **Complexity**: The complexity of implementing and managing a topology.

## Comparison

| Topology | Reliability | Scalability | Cost | Use Case |
|---|---|---|---|---|
| **[Bus](./bus)** | Low | Low | Low | Small networks |
| **[Star](./star)** | Medium | Low | Medium | Local area networks (LANs) |
| **[Ring](./ring)** | High | Low | Medium | Telecom networks |
| **[Mesh](./mesh)** | High | High | High | Wide area networks (WANs) |
| **[Tree](./tree)** | Medium | High | High | Large networks |

## Trade-offs

- **Reliability vs. Cost**: More reliable topologies are often more expensive.
- **Scalability vs. Complexity**: More scalable topologies are often more complex.
- **Performance vs. Cost**: Higher performance topologies are often more expensive.

## Which service use it?



-   **Bus Topology:** Historically used in early Ethernet networks (e.g., 10Base2, 10Base5 coaxial cables) and still found in some industrial control systems or embedded networks.

-   **Star Topology:** Widely used in modern Local Area Networks (LANs) where all devices connect to a central switch or hub. Most home and office networks are star topologies.

-   **Ring Topology:** Historically used in Token Ring networks and some fiber optic networks. Also found in some Storage Area Networks (SANs) and metropolitan area networks (MANs).

-   **Mesh Topology:** Employed in critical infrastructure like military communications, backbone networks of the internet, and some wireless sensor networks where high redundancy and fault tolerance are paramount.

-   **Tree Topology:** Often used in large corporate networks, combining multiple star networks into a hierarchical structure, allowing for easy expansion and management.

## Related Concepts

-   **Communication:** The network topology fundamentally defines the paths and patterns through which nodes in a distributed system communicate, directly impacting latency, bandwidth, and message delivery. [Explore Communication Patterns](../communication/README.md).

-   **Fault Tolerance:** The choice of topology significantly influences a system's fault tolerance, determining its resilience to node or link failures and how quickly it can recover or reroute traffic. [Understand Fault Tolerance](../fault-tolerance/README.md).

-   **Scaling:** Topology plays a crucial role in how easily a distributed system can scale, as some arrangements are more conducive to adding new nodes and distributing workload efficiently than others. [Learn about Scaling](../scaling/README.md).

-   **System Modes:** Different distributed system architectures or modes (e.g., client-server, peer-to-peer) often implicitly or explicitly adopt certain network topologies that best suit their operational model and requirements. [Discover System Modes](../system-mode/README.md).

-   **Distributed Consensus:** The underlying network topology can affect the performance, reliability, and even the feasibility of distributed consensus algorithms, as message propagation and failure detection are topology-dependent. [Understand Distributed Consensus](../distributed-consensus/README.md).
