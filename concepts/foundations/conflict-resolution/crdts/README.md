# CRDTs (Conflict-free Replicated Data Types) for Conflict Resolution

## Core

This section details how CRDTs are designed to resolve conflicts automatically and deterministically, making them suitable for collaborative and eventually consistent distributed systems.

### How CRDTs Work

CRDTs achieve conflict-free replication by ensuring that concurrent operations commute, meaning the order in which they are applied does not affect the final state. There are two main types of CRDTs:

1.  **Operation-based CRDTs (CmRDTs - Commutative Replicated Data Types):**
    *   These CRDTs transmit operations (e.g., "increment by 1", "add element X").
    *   Each operation is applied locally and then broadcast to other replicas.
    *   The operations must be commutative, meaning `op1(op2(state))` yields the same result as `op2(op1(state))`.
    *   They require reliable, causally ordered message delivery.

2.  **State-based CRDTs (CvRDTs - Convergent Replicated Data Types):**
    *   These CRDTs transmit their full local state (or a merge of states).
    *   When a replica receives a state from another replica, it merges it with its own state using a join function (least upper bound) that is commutative, associative, and idempotent.
    *   They only require eventual message delivery, as states can be merged in any order.

Both types guarantee strong eventual consistency: all replicas will eventually converge to the same state, even with concurrent updates and network partitions, without requiring complex coordination protocols or manual conflict resolution.

## Characteristics

- **Conflict-free**: CRDTs are designed to be conflict-free, meaning that they can be updated concurrently without requiring a central authority to resolve conflicts.
- **Convergent**: CRDTs are convergent, meaning that all replicas will eventually converge to the same state.
- **Commutative**: The order in which updates are applied does not matter.
- **Associative**: Updates can be grouped together in any way.
- **Idempotent**: Applying the same update multiple times has the same effect as applying it once.

## Trade-offs

- **Complexity vs. Power**: CRDTs are more complex than other conflict resolution strategies, but they are also more powerful.
- **Performance vs. Correctness**: CRDTs can have a performance overhead, but they can ensure correctness in the presence of concurrent updates.

## Which service use it?

-   **Collaborative Text Editors:** Applications like Google Docs or Atom Teletype use CRDTs to allow multiple users to edit the same document concurrently without explicit locking, and changes are merged automatically.

-   **Shared Whiteboards and Drawing Applications:** CRDTs can manage concurrent drawing operations, ensuring that all users see a consistent final state.

-   **Distributed Counters and Sets:** In scenarios where multiple nodes need to update a shared counter or a set of items, CRDTs provide a way to do this without conflicts, ensuring eventual consistency.

-   **Multiplayer Games:** CRDTs can be used to synchronize game state across multiple players, especially for elements where concurrent updates are common and need to be resolved smoothly.

-   **Offline-First Applications:** Mobile or web applications that need to function offline and synchronize changes when connectivity is restored can leverage CRDTs for seamless merging of user-generated data.
