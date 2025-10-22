# CRDTs (Conflict-free Replicated Data Types)

## Core

This section introduces CRDTs as a mechanism for coordination in distributed systems, allowing concurrent updates without conflicts.

## Comparison

| Feature | Description |
|---|---|
| **Conflict Resolution** | Automatic and deterministic. |
| **Consistency** | Eventual consistency. |
| **Complexity** | Can be complex to design and implement. |
| **Use Case** | Collaborative editing, shared data structures. |

## Which service use it?



-   **Collaborative Text Editors:** Applications like Google Docs or Atom Teletype use CRDTs to allow multiple users to edit the same document concurrently without explicit locking, and changes are merged automatically.

-   **Shared Whiteboards and Drawing Applications:** CRDTs can manage concurrent drawing operations, ensuring that all users see a consistent final state.

-   **Distributed Counters and Sets:** In scenarios where multiple nodes need to update a shared counter or a set of items, CRDTs provide a way to do this without conflicts, ensuring eventual consistency.

-   **Multiplayer Games:** CRDTs can be used to synchronize game state across multiple players, especially for elements where concurrent updates are common and need to be resolved smoothly.

-   **Offline-First Applications:** Mobile or web applications that need to function offline and synchronize changes when connectivity is restored can leverage CRDTs for seamless merging of user-generated data.

## Related Concepts

-   **Conflict Resolution:** CRDTs are a powerful approach to conflict resolution in distributed systems, specifically designed to allow concurrent updates to shared data without requiring complex coordination or centralized control. [Explore other Conflict Resolution strategies](../../conflict-resolution/README.md).

-   **Eventual Consistency:** CRDTs inherently provide eventual consistency, guaranteeing that all replicas will eventually converge to the same state, given enough time and communication, without requiring strong consistency mechanisms. [Learn more about Eventual Consistency](../../consistency-models/eventual-consistency/README.md).

-   **Data Replication:** CRDTs are typically employed in scenarios involving data replication, where multiple copies of data exist across different nodes, and updates need to be propagated and merged reliably. [Understand Data Replication](../../data-replication/README.md).

-   **Coordination:** As a mechanism for managing shared state in a distributed environment, CRDTs serve as a form of coordination, enabling independent operations on data that eventually converge. [Discover other Coordination techniques](../README.md).
