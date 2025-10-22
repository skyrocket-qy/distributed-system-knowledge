# Communication

## Core

In distributed systems, **communication** is the mechanism by which processes running on different nodes interact and exchange information. Effective communication is fundamental to the functioning of any distributed system, as it enables coordination, data sharing, and the execution of distributed algorithms.

This section explores various communication patterns, protocols, and models used for inter-process communication. Key challenges in distributed communication include handling network latency, ensuring message delivery, maintaining order, and dealing with failures, which are often addressed through concepts discussed in [Consistency Models](../consistency-models/README.md) and [Fault Tolerance](../fault-tolerance/README.md).

### Key Challenges

-   **Network Latency:** The delay introduced by the time it takes for data to travel across the network.
    *   **Interconnection:** Often mitigated by techniques discussed in [Data Replication](../data-replication/README.md) (e.g., placing data closer to users) and efficient [Topology](../topology/README.md) design.

-   **Message Loss:** Messages can be dropped due to network congestion, hardware failures, or other issues.
    *   **Interconnection:** Addressed through reliable messaging patterns (e.g., acknowledgments, retries) often implemented within [Messaging](../messaging/README.md) systems like Message Queues, and considered in [Fault Tolerance](../fault-tolerance/README.md) strategies.

-   **Message Ordering:** Ensuring messages are processed in the order they were sent, especially across different nodes.
    *   **Interconnection:** Crucial for maintaining [Consistency Models](../consistency-models/README.md) and often managed using mechanisms like logical clocks or sequence numbers, which relate to [Coordination](../coordination/README.md) and [Distributed Transactions](../distributed-transactions/README.md).

-   **Partial Failures:** One part of the system failing while others continue to operate, leading to inconsistent states.
    *   **Interconnection:** A core concern for [Fault Tolerance](../fault-tolerance/README.md), often requiring robust [Distributed Consensus](../distributed-consensus/README.md) algorithms and careful design of [System Modes](../system-mode/README.md) (e.g., active-passive, active-active).

-   **Security:** Protecting communication channels from eavesdropping, tampering, and unauthorized access.
    *   **Interconnection:** A dedicated concern within the [Security](../security/README.md) topic, involving encryption, authentication, and authorization mechanisms applied to communication protocols.

## Characteristics

- **Scalability:** The ability to handle a growing number of messages and nodes.
- **Fault Tolerance:** The system's resilience to node or network failures.
- **Consistency:** Guarantees about the ordering and visibility of messages.
- **Security:** Measures to protect data during transit.

## Comparison

| Pattern | Coupling | Synchronicity | Topology | Use Case |
|---|---|---|---|---|
| **[Client-Server](./client-server)** | Tight | Synchronous | Centralized | Web services, databases |
| **[Message Queue](./message-queue)** | Loose | Asynchronous | Decoupled | Task processing, microservices |
| **[Publish-Subscribe](./pubsub)** | Loose | Asynchronous | Decoupled | Event-driven systems, notifications |
| **[Peer-to-Peer (P2P)](./p2p)** | Loose | Both | Decentralized | File sharing, content delivery |
| **[Actor Model](./actor-model)** | Loose | Asynchronous | Decentralized | Concurrent and parallel systems |

## Trade-offs

| Pattern | Advantages | Disadvantages |
|---|---|---|
| **Client-Server** | Simple to implement, centralized control | Single point of failure, scalability bottlenecks |
| **Message Queue** | Decoupling, scalability, fault tolerance | Increased complexity, potential for latency |
| **Publish-Subscribe** | Scalability, flexibility, loose coupling | Message ordering challenges, potential for message loss |
| **Peer-to-Peer** | Decentralized, fault-tolerant, scalable | Complex to manage, security concerns |
| **Actor Model** | High concurrency, fault isolation | Complex programming model, potential for deadlocks |

## Which service use it?



-   **Client-Server:** The most common communication pattern, used in virtually all web applications, email systems, file servers, and traditional enterprise software.

-   **Message Queue:** Asynchronous task processing, decoupling microservices, buffering requests, and enabling reliable communication between distributed components.

-   **Publish-Subscribe:** Real-time data feeds, event notifications, chat applications, and IoT data ingestion.

-   **Peer-to-Peer (P2P):** File sharing networks, cryptocurrencies, distributed content delivery, and some online gaming.

-   **Actor Model:** Concurrent and parallel systems, especially those requiring high concurrency and fault tolerance, such as Erlang/OTP applications, Akka-based systems, and some distributed databases.
