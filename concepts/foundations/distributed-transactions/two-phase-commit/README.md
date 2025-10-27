# Two-Phase Commit (2PC)

## Core

**Two-Phase Commit (2PC)** is a classic atomic commitment protocol that ensures all participating nodes in a distributed transaction either commit or abort the transaction together. It is designed to guarantee atomicity across multiple participants, even in the face of failures.

The protocol involves a coordinator and multiple participants. It operates in two distinct phases:

```mermaid
sequenceDiagram
    participant C as Coordinator
    participant P1 as Participant 1
    participant P2 as Participant 2

    C->>P1: Prepare?
    C->>P2: Prepare?

    alt All Participants can commit
        P1-->>C: Vote Commit
        P2-->>C: Vote Commit
        C->>P1: Global Commit
        C->>P2: Global Commit
        P1-->>C: Acknowledgment
        P2-->>C: Acknowledgment
    else Any Participant votes Abort or Fails
        P1-->>C: Vote Abort
        C->>P1: Global Abort
        C->>P2: Global Abort
        P1-->>C: Acknowledgment
        P2-->>C: Acknowledgment
    end
```

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

## Characteristics

- **Blocking**: 2PC is a blocking protocol; if the coordinator fails, participants may be blocked and unable to proceed.
- **Atomic**: All participants either commit or abort the transaction.
- **Consistent**: The protocol ensures that all participants reach a consistent decision.
- **Durable**: The outcome of the transaction is durable, even in the case of failures.
- **Centralized**: The protocol relies on a central coordinator to make the final decision.


## Pros & Cons

### Pros
-   **Atomicity and Consistency:** Guarantees that all participating nodes either commit or abort the transaction together, ensuring data consistency across distributed systems.
-   **Simplicity (Relative):** Compared to more complex distributed consensus algorithms, the basic concept of 2PC is relatively straightforward to understand.
-   **Durability:** Once committed, the changes are permanent and survive failures.

### Cons
-   **Blocking Protocol:** This is the most significant drawback. If the coordinator fails after the "prepare" phase but before sending the "commit" or "abort" message, participants can remain indefinitely blocked, holding resources.
-   **Single Point of Failure (Coordinator):** The coordinator is central to the protocol. Its failure can leave transactions in an "in-doubt" state, requiring manual intervention.
-   **Performance Overhead:** Involves multiple rounds of communication, leading to increased latency and reduced throughput, especially in high-latency networks or with many participants.
-   **Scalability Limitations:** Due to its synchronous and blocking nature, 2PC can struggle with scalability in large-scale distributed systems.
-   **Not Fully Resilient:** While it handles some failures, it's not robust against all possible failure scenarios, particularly concurrent failures of the coordinator and participants.

## Use Case

-   **Distributed Databases:** Used in traditional distributed relational databases (e.g., XA transactions in Oracle, SQL Server) to maintain ACID properties across multiple database instances.
-   **Enterprise Systems:** Employed in enterprise application servers and transaction processing monitors where strong consistency and atomicity are critical for business operations.

