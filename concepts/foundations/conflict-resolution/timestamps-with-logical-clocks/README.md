# Timestamps with Logical Clocks for Conflict Resolution

## Core

This section explains how timestamps combined with logical clocks (e.g., Lamport timestamps, Vector Clocks) are used to resolve conflicts in distributed systems by establishing a causal order of events.

## Comparison

| Feature | Description |
|---|---|
| **Causal Ordering** | Establishes a partial order of events. |
| **Conflict Detection** | Can detect concurrent updates. |
| **Complexity** | More complex than simple LWW, but less than CRDTs. |
| **Implementation** | Requires careful management of clock values. |

## Which service use it?



-   **Distributed Databases:** Many distributed databases use logical clocks (like Lamport timestamps or vector clocks) internally to order events and resolve conflicts, especially in eventually consistent or multi-master replication scenarios.

-   **Event Sourcing Systems:** In event-sourced architectures, logical clocks can be used to ensure the correct ordering of events in the event log, which is crucial for reconstructing the state of an aggregate.

-   **Distributed Transaction Systems:** While complex, some distributed transaction protocols might leverage logical clocks to help in ordering operations and ensuring consistency across multiple participating nodes.

-   **Distributed Caching:** When multiple caches can be updated concurrently, logical clocks can help in determining the most recent version of a cached item.

## Related Concepts

-   **Conflict Resolution:** Timestamps with logical clocks provide a mechanism for conflict resolution by establishing a causal or total order of events, allowing systems to determine which update "happened after" another. [Explore other Conflict Resolution strategies](../README.md).

-   **Vector Clocks:** Vector clocks are a more sophisticated type of logical clock that can directly detect concurrency, offering stronger guarantees for causal ordering and conflict detection than simple Lamport timestamps. [Compare with Vector Clocks](../vector-clocks/README.md).

-   **Last-Write-Wins (LWW):** While LWW often relies on simple physical timestamps, logical clocks provide a more robust way to determine the "last write" by considering causal relationships, especially in eventually consistent systems. [Compare with Last-Write-Wins](../last-write-wins/README.md).

-   **Causal Consistency:** Logical clocks, particularly vector clocks, are fundamental to implementing causal consistency, ensuring that causally related operations are observed in the correct order across a distributed system. [Explore Causal Consistency](../../consistency-models/causal-consistency/README.md).

-   **Coordination:** Logical clocks serve as a coordination mechanism by providing a consistent way to order events across distributed nodes, which is crucial for maintaining data integrity and resolving conflicts. [Discover Coordination Concepts](../../coordination/README.md).

## Trade-offs
