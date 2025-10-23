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

| Model | Guarantee | Performance | Staleness | Debug Complexity | Implementation Complexity | Use Case |
|---|---|---|---|---|---|---|
| **[Strong Consistency](./strong-consistency)** | All replicas are always up-to-date | High latency (due to coordination overhead) | No | Low | High | Financial systems, critical data |
| **[Sequential Consistency](./sequential)** | All operations appear to execute in a single, global order, preserving program order. | High latency (due to strict global ordering and coordination) | No | Medium | High | Distributed shared memory, critical sections |
| **[Eventual Consistency](./eventual-consistency)** | Replicas will eventually be consistent | Low latency (allows for faster writes) | Yes | High | Low | Social media, e-commerce |
| **[Causal Consistency](./causal-consistency)** | Causal order of operations is preserved | Medium latency (requires tracking causal dependencies) | Yes | High | Medium | Collaborative editing, chat |


