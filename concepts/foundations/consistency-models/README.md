# Consistency Models

## Core

In a distributed system, a **consistency model** is a contract between the system and the application that specifies the guarantees the system will provide regarding the visibility and ordering of updates to data. When data is replicated across multiple nodes, it's not always possible to ensure that all clients see the same data at the same time. A consistency model defines the rules for how and when the system will propagate updates and make them visible to clients.

The choice of a consistency model has a significant impact on the performance, availability, and complexity of a distributed system. There is often a trade-off between the strength of the consistency guarantee and the performance and availability of the system. Stronger consistency models are easier for developers to reason about, but they often come at the cost of higher latency and lower availability. Weaker consistency models can provide better performance and availability, but they require developers to handle the complexities of eventual consistency.

### Key Considerations

-   **Application Requirements:** The specific needs of the application regarding data accuracy, freshness, and user experience.
-   **Performance vs. Consistency:** The inherent trade-off between providing strong consistency guarantees and achieving high performance and availability.
-   **Developer Complexity:** The ease or difficulty for developers to reason about and work with a given consistency model.
-   **Conflict Resolution:** How conflicts arising from concurrent updates are handled, especially in weaker consistency models.
-   **Network Partitions:** The system's behavior and data availability during network failures that partition the system.

## Comparison

| Model | Guarantee | Performance | Use Case |
|---|---|---|---|
| **[Strong Consistency](./strong-consistency)** | All replicas are always up-to-date | High latency (due to coordination overhead) | Financial systems, critical data |
| **[Eventual Consistency](./eventual-consistency)** | Replicas will eventually be consistent | Low latency (allows for faster writes) | Social media, e-commerce |
| **[Causal Consistency](./causal-consistency)** | Causal order of operations is preserved | Medium latency (requires tracking causal dependencies) | Collaborative editing, chat |

## Trade-offs

| Model | Advantages | Disadvantages |
|---|---|---|
| **Strong Consistency** | Simplifies application development, predictable behavior | Higher latency, lower availability |
| **Eventual Consistency** | High availability, low latency for writes | More complex for developers, potential for stale data |
| **Causal Consistency** | Good balance, preserves logical order | More complex than eventual, dependency tracking overhead |

## Which service use it?



-   **Strong Consistency:** Financial transaction systems, banking applications, and critical data management systems where immediate data accuracy is paramount.

-   **Eventual Consistency:** Social media feeds, e-commerce product catalogs, DNS, and large-scale web services where high availability and performance are prioritized over immediate consistency.

-   **Causal Consistency:** Collaborative editing applications, distributed social networks, and systems that need to preserve the causal order of events without requiring global strong consistency.

## Related Concepts

-   **[Data Replication](../../patterns/data-replication/README.md):** The choice of a consistency model directly influences how data is replicated across multiple nodes and how those replicas are kept in sync. Stronger consistency often requires more complex replication strategies.
-   **[Distributed Transactions](../distributed-transactions/README.md):** Ensuring ACID properties in distributed transactions heavily relies on the underlying consistency model. Weaker consistency models often lead to alternative transaction patterns like Sagas.
-   **[CAP Theorem](../system-mode/cap-tradeoff-tunable/README.md):** A foundational principle stating that a distributed data store cannot simultaneously provide more than two out of Consistency, Availability, and Partition tolerance. Consistency models represent different trade-offs within the CAP theorem.
-   **[Distributed Consensus](../distributed-consensus/README.md):** Algorithms like Paxos and Raft are often employed to achieve strong consistency across distributed systems by ensuring all nodes agree on a single state or order of operations.
-   **[Conflict Resolution](../conflict-resolution/README.md):** In systems with weaker consistency models (e.g., eventual consistency), mechanisms for conflict resolution become crucial to merge divergent data states gracefully.
-   **[Coordination](../coordination/README.md):** The chosen consistency model dictates the level and type of coordination required between nodes to maintain data integrity and visibility across the distributed system.
