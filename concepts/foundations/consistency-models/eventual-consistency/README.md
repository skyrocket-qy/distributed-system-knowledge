# Eventual Consistency

## Core

This section describes the eventual consistency model, where the system guarantees that if no new updates are made to a given data item, eventually all accesses to that item will return the last updated value.

## Characteristics

- **High Availability**: Eventual consistency provides high availability, as it allows the system to continue operating even in the presence of network partitions.
- **Low Latency**: Eventual consistency allows for low-latency reads and writes, as operations can be performed on local replicas without waiting for coordination with other nodes.
- **Scalability**: Eventual consistency is highly scalable, as it allows new nodes to be added to the system without requiring a global re-synchronization.
- **Stale Reads**: Eventual consistency can result in stale reads, as a read operation may return a value that is not the most recent write.
- **Conflict Resolution**: Eventual consistency requires a mechanism to resolve conflicts that can arise from concurrent writes to different replicas.

## Comparison

| Feature | Description |
|---|---|
| **Guarantee** | Eventually all replicas will converge to the same state. |
| **Availability** | High availability, even during network partitions. |
| **Performance** | High write and read performance. |
| **Complexity** | Developers need to handle potential inconsistencies. |

## Trade-offs

- **Availability vs. Consistency**: Eventual consistency trades off consistency for availability.
- **Performance vs. Consistency**: Eventual consistency provides better performance than strong consistency.
- **Simplicity vs. Complexity**: Eventual consistency is more complex to reason about than strong consistency.

## Which service use it?

-   **Domain Name System (DNS):** DNS is a classic example where updates to records propagate across the internet over time, leading to eventual consistency.
-   **Amazon S3 (Simple Storage Service):** S3 provides eventual consistency for most operations, meaning that a read immediately after a write might not reflect the latest version.
-   **NoSQL Databases (e.g., Apache Cassandra, Amazon DynamoDB):** Many NoSQL databases prioritize availability and partition tolerance over strong consistency, offering eventual consistency as their primary model.
-   **Social Media Feeds:** Updates to user feeds (e.g., Facebook, Twitter) are eventually consistent, meaning a new post might not appear immediately for all followers.
-   **E-commerce Shopping Carts:** While critical operations like checkout are strongly consistent, the display of items in a shopping cart might be eventually consistent to improve performance.

## Related Concepts

-   **Conflict Resolution (CRDTs):** Eventual consistency often leads to conflicts when concurrent updates occur. Conflict-free Replicated Data Types (CRDTs) are data structures that can be replicated across multiple servers, allowing concurrent updates without requiring complex coordination, and automatically resolving conflicts in a mathematically sound way. [Learn more about CRDTs](../conflict-resolution/crdts/README.md).

-   **Asynchronous Data Replication:** Eventual consistency is commonly achieved through asynchronous replication strategies, where updates are propagated to replicas with some delay, rather than immediately. [Explore Asynchronous Replication](../../data-replication/async/README.md).

-   **CAP Theorem:** Eventual consistency is a choice made when prioritizing Availability and Partition Tolerance over strong Consistency, as described by the CAP theorem. [Understand the CAP Theorem](../../system-mode/cap-tradeoff-tunable/README.md).

-   **Strong Consistency:** In contrast to eventual consistency, strong consistency guarantees that all reads return the most recent write, but often at the cost of availability or partition tolerance. [Compare with Strong Consistency](../strong-consistency/README.md).
