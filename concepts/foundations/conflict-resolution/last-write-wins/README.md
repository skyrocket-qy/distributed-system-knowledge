# Last Write Wins (LWW) for Conflict Resolution

## Core

This section describes the Last Write Wins (LWW) strategy for conflict resolution, where the most recent write operation (based on a timestamp) is chosen as the definitive version, discarding older conflicting writes.

## Comparison

| Feature | Description |
|---|---|
| **Simplicity** | Easy to implement and understand. |
| **Data Loss** | Potential for data loss if an older, semantically important write is overwritten. |
| **Performance** | Generally high, as it avoids complex merge logic. |
| **Dependency** | Relies on accurate timestamps across distributed nodes. |

## Which service use it?



-   **Eventually Consistent Key-Value Stores:** Many NoSQL databases that prioritize availability and partition tolerance (e.g., some configurations of Apache Cassandra, Amazon DynamoDB) use LWW as a default or configurable conflict resolution strategy.

-   **Caching Systems:** When multiple clients update the same cached item, the last update often overwrites previous ones, especially in distributed caches.

-   **Simple Data Synchronization:** In scenarios where data loss from concurrent updates is acceptable or rare, and a simple resolution mechanism is preferred, LWW can be used.

-   **Session Management:** In distributed web applications, if multiple requests update a user's session data concurrently, LWW might be used to ensure the most recent session state is preserved.

## Related Concepts

-   **Conflict Resolution:** Last Write Wins (LWW) is a straightforward conflict resolution strategy that prioritizes the most recent update based on a timestamp, making it simple to implement but potentially leading to data loss. [Explore other Conflict Resolution strategies](../README.md).

-   **Timestamps with Logical Clocks:** LWW heavily relies on timestamps to determine the "latest" write. While physical timestamps are often used, logical clocks can provide a more robust causal ordering, especially in distributed environments. [Learn about Timestamps with Logical Clocks](../timestamps-with-logical-clocks/README.md).

-   **Vector Clocks:** In contrast to LWW, vector clocks are designed to detect concurrent updates rather than simply overwriting them, allowing for more sophisticated application-level conflict resolution or merging. [Compare with Vector Clocks](../vector-clocks/README.md).

-   **Eventual Consistency:** LWW is a common conflict resolution mechanism employed in eventually consistent systems, where replicas may temporarily diverge, and the system relies on a simple rule to converge to a final state. [Understand Eventual Consistency](../../consistency-models/eventual-consistency/README.md).

-   **Data Replication:** LWW is frequently applied in replicated data scenarios, particularly in multi-master or asynchronous replication setups, where concurrent writes to the same data item across different replicas are possible. [Understand Data Replication](../../data-replication/README.md).
