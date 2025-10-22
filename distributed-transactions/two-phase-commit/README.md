# Two-Phase Commit (2PC)

## Core

**Two-Phase Commit (2PC)** is a classic atomic commitment protocol that ensures all participating nodes in a distributed transaction either commit or abort the transaction together. It is designed to guarantee atomicity across multiple participants, even in the face of failures.

The protocol involves a coordinator and multiple participants. It operates in two distinct phases:

### Phase 1: Commit-Request (Vote) Phase

1.  **Coordinator sends prepare message:** The coordinator sends a "prepare" message to all participants, asking them to prepare to commit the transaction.
2.  **Participants vote:** Each participant executes the transaction up to the point of committing and writes all changes to a local undo log and a redo log. If a participant can successfully prepare, it replies with a "vote-commit" message to the coordinator and waits for the coordinator's decision. If it cannot prepare (e.g., due to a local failure or constraint violation), it replies with a "vote-abort" message.

### Phase 2: Commit Phase

1.  **Coordinator collects votes:** The coordinator collects all votes from the participants.
    *   **If all participants vote-commit:** The coordinator sends a "global-commit" message to all participants.
    *   **If any participant votes-abort (or fails to respond within a timeout):** The coordinator sends a "global-abort" message to all participants.
2.  **Participants act on decision:**
    *   **If global-commit:** Participants commit their local transaction and release any held resources. They then send an "acknowledgment" to the coordinator.
    *   **If global-abort:** Participants roll back their local transaction using the undo log and release any held resources. They then send an "acknowledgment" to the coordinator.
3.  **Coordinator finalizes:** The coordinator waits for acknowledgments from all participants before finalizing the transaction.

## Trade-offs

-   **High Latency:** The two-phase communication and blocking nature introduce significant latency, especially with many participants or high network delays.
-   **Blocking:** Participants hold resources (e.g., locks) during the entire protocol, which can lead to reduced concurrency and potential deadlocks if the coordinator fails.
-   **Single Point of Failure:** If the coordinator fails during the commit phase, participants may be left in an uncertain state, unable to commit or abort until the coordinator recovers or a recovery protocol is initiated.

## Use Case

-   **Distributed Databases:** Used in traditional distributed relational databases (e.g., XA transactions in Oracle, SQL Server) to maintain ACID properties across multiple database instances.
-   **Enterprise Systems:** Employed in enterprise application servers and transaction processing monitors where strong consistency and atomicity are critical for business operations.

## Related Concepts

-   **Distributed Transactions:** Two-Phase Commit (2PC) is a foundational protocol for ensuring atomicity and consistency across multiple participants in a distributed transaction. [Explore Distributed Transactions](../README.md).

-   **Three-Phase Commit (3PC):** 2PC is often compared with Three-Phase Commit (3PC), which attempts to mitigate some of 2PC's blocking issues and single points of failure, though at the cost of increased complexity. [Compare with Three-Phase Commit](../three-phase-commit/README.md).

-   **Saga Pattern:** In modern distributed systems, particularly microservices, the Saga pattern is often preferred over 2PC as an alternative for managing consistency across services, trading strong consistency for eventual consistency and improved availability. [Explore the Saga Pattern](../saga-pattern/README.md).

-   **Distributed Consensus:** Atomic commitment protocols like 2PC are fundamentally a form of distributed consensus, where all participating nodes must agree on whether to commit or abort a transaction. [Understand Distributed Consensus](../../distributed-consensus/README.md).

-   **Fault Tolerance:** 2PC has known limitations regarding fault tolerance, particularly its blocking nature and the coordinator being a single point of failure, which can lead to participants being stuck in an uncertain state. [Learn about Fault Tolerance](../../fault-tolerance/README.md).

-   **Strong Consistency:** Protocols like 2PC are designed to achieve strong consistency across distributed data, ensuring that all participants see the same state after a transaction is committed. [Explore Strong Consistency](../../consistency-models/strong-consistency/README.md).
