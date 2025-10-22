# Star Topology

## Core

This section explains the Star topology in distributed systems. In a star topology, all nodes are connected to a central hub.

## Characteristics

- **Centralized**: All nodes are connected to a central hub.
- **Simplicity**: Star topology is simple to install and manage.
- **Reliability**: The failure of a single node does not affect the rest of the network.
- **Scalability**: It is easy to add new nodes to the network.
- **Single Point of Failure**: The central hub is a single point of failure.

## Comparison

| Topology | Reliability | Scalability | Cost | Complexity |
|---|---|---|---|---|
| **Star** | Medium | Medium | Medium | Medium |
| **Bus** | Low | Low | Low | Low |
| **Ring** | Medium | Low | Medium | Medium |
| **Mesh** | High | Low | High | High |

## Trade-offs

- **Reliability vs. Single Point of Failure**: The failure of a single node does not affect the rest of the network, but the central hub is a single point of failure.
- **Scalability vs. Performance**: It is easy to add new nodes to the network, but the performance of the network can degrade as more nodes are added.

## Which service use it?



-   **Local Area Networks (LANs):** The most common topology for modern wired LANs, where all computers and network devices connect to a central switch or hub.

-   **Client-Server Architectures:** In a client-server model, the server acts as the central hub, and all clients connect to it to request services.

-   **Centralized Monitoring Systems:** Monitoring agents on various machines report to a central monitoring server, forming a star-like communication pattern.

-   **Home Networks:** Most home Wi-Fi networks are essentially star topologies, with all devices connecting to the central router.

-   **Cloud Computing (Conceptual):** In many cloud deployments, virtual machines or containers communicate with central services (e.g., load balancers, databases, API gateways) in a star-like fashion.

## Related Concepts

-   **Topology:** Star topology is a common network arrangement where all nodes connect to a central hub, simplifying management and fault isolation for individual nodes. [Explore other Network Topologies](../README.md).

-   **Tree Topology:** Star topologies often form the building blocks of larger, hierarchical tree topologies, where multiple star networks are interconnected through higher-level hubs. [Compare with Tree Topology](../tree/README.md).

-   **Client-Server Communication:** The star topology is a natural fit for client-server architectures, with the server acting as the central hub to which all clients connect for services. [Understand Client-Server Communication](../../communication/client-server/README.md).

-   **Fault Tolerance:** While individual node failures do not affect the rest of the network in a star topology, the central hub represents a single point of failure, making its reliability critical for overall system fault tolerance. [Understand Fault Tolerance](../../fault-tolerance/README.md).

-   **Communication:** The star topology dictates that all communication between peripheral nodes must pass through the central hub, influencing communication latency and potential bottlenecks. [Explore Communication Patterns](../../communication/README.md).
