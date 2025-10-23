# Conflict Resolution

## Core

**Conflict resolution** is the process of managing and resolving inconsistencies that arise when multiple nodes in a distributed system attempt to update the same piece of data concurrently. In any system where data is replicated and can be modified in more than one location, conflicts are inevitable.

Without robust conflict resolution mechanisms, a distributed system can suffer from data divergence, where replicas of the same data become inconsistent over time. This can lead to data corruption, incorrect application behavior, and a violation of the system's integrity guarantees. This is a particularly important challenge in eventually consistent systems.

This section addresses various strategies and mechanisms for resolving these conflicts, including:
- **Last-Write-Wins (LWW):** A simple approach where the update with the latest timestamp is chosen as the winner.
- **Vector Clocks:** A more sophisticated mechanism that can detect concurrent updates and leave the resolution to the application.
- **Conflict-free Replicated Data Types (CRDTs):** Data structures designed for concurrent modification without conflicts, often used in [Data Replication](../data-replication/README.md) and as a [Coordination](../coordination/README.md) mechanism.
- **Application-specific Logic:** In some cases, the application itself is best equipped to resolve conflicts based on business rules.

### Considerations

-   **Data Semantics:** The nature of the data and the meaning of concurrent updates (e.g., merging text vs. financial transactions).
-   **Application Requirements:** The acceptable level of data loss, consistency guarantees, and user experience.
-   **Performance Overhead:** The computational and network resources required by the chosen resolution strategy.
-   **Complexity:** The difficulty of implementing and maintaining the conflict resolution mechanism.
-   **Determinism:** Whether the resolution process always yields the same result given the same set of conflicting updates.

## Characteristics

- **Conflict Detection**: The ability to detect when two or more updates conflict with each other.
- **Conflict Resolution**: The process of resolving a conflict and choosing a winning update.
- **Data Convergence**: The process of ensuring that all replicas of the data eventually converge to the same state.
- **Data Loss**: The possibility of losing data during conflict resolution.
- **Complexity**: The complexity of the conflict resolution algorithm.

## Comparison

| Strategy | Complexity | Data Loss Risk | Resolution Logic | Use Case |
|---|---|---|---|---|
| **[Last-Write-Wins (LWW)](./last-write-wins)** | Low | High | Timestamp-based | Simple, non-critical data |
| **[Vector Clocks](./vector-clocks)** | Medium | Low | Causal history | Detecting concurrency, manual resolution |
| **[CRDTs](./crdts)** | High | None | Automatic, deterministic | Collaborative editing, real-time apps |
| **[Timestamps with Logical Clocks](./timestamps-with-logical-clocks)** | Medium | Medium | Causal ordering | Distributed databases, event sourcing |

## Trade-offs

| Strategy | Advantages | Disadvantages |
|---|---|---|
| **Last-Write-Wins (LWW)** | Simple, low overhead | Potential for data loss, relies on synchronized clocks |
| **Vector Clocks** | Detects concurrency, prevents data loss | Increased complexity, requires application-level resolution |
| **CRDTs** | Automatic resolution, no data loss | High complexity, limited data types |
| **Timestamps with Logical Clocks** | Causal ordering, prevents data loss | Increased overhead, requires clock synchronization |

## Which service use it?



-   **Last-Write-Wins (LWW):** Often used in systems where simplicity is prioritized and occasional data loss due to concurrent updates is acceptable, such as caching systems or some eventually consistent key-value stores.

-   **Vector Clocks:** Employed in distributed databases (e.g., Riak) and collaborative systems to detect concurrent updates and allow for application-level conflict resolution or merging.

-   **CRDTs (Conflict-free Replicated Data Types):** Ideal for real-time collaborative applications (e.g., text editors, whiteboards) where multiple users can concurrently modify data, and conflicts need to be resolved automatically and deterministically.

-   **Timestamps with Logical Clocks:** Used in distributed databases and event sourcing systems to establish a causal order of events and resolve conflicts based on that order, providing stronger consistency guarantees than simple physical timestamps.

-   **Application-specific Logic:** Many complex distributed systems, especially those dealing with business logic, implement custom conflict resolution strategies tailored to their specific domain requirements.
