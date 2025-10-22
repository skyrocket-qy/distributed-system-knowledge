# Three-Phase Commit (3PC)

## Core

**Three-Phase Commit (3PC)** is an atomic commitment protocol designed to address some of the blocking issues inherent in Two-Phase Commit (2PC), particularly in the event of a coordinator failure. It adds an extra phase to 2PC to ensure that participants are not left in an uncertain state if the coordinator crashes after sending a commit message but before all participants receive it.

Like 2PC, 3PC involves a coordinator and multiple participants. It operates in three distinct phases:

### Phase 1: CanCommit? Phase

1.  **Coordinator sends CanCommit? message:** The coordinator sends a "CanCommit?" message to all participants, asking if they are ready to commit the transaction.
2.  **Participants respond:** Each participant performs necessary checks and, if ready, replies with a "Yes" message. Otherwise, it replies with a "No" message.

### Phase 2: PreCommit Phase

1.  **Coordinator collects responses:**
    *   **If all participants respond "Yes":** The coordinator sends a "PreCommit" message to all participants.
    *   **If any participant responds "No" (or fails to respond within a timeout):** The coordinator sends an "Abort" message to all participants, and the transaction is aborted.
2.  **Participants prepare to commit:** Upon receiving "PreCommit," participants prepare to commit the transaction (e.g., by writing to stable storage) and send an "Ack" message to the coordinator.

### Phase 3: DoCommit Phase

1.  **Coordinator collects Acks:**
    *   **If all participants send "Ack":** The coordinator sends a "DoCommit" message to all participants.
    *   **If any participant fails to send "Ack" (or fails to respond within a timeout):** The coordinator sends an "Abort" message to all participants, and the transaction is aborted.
2.  **Participants commit:** Upon receiving "DoCommit," participants commit the transaction and release resources. They then send a "Done" message to the coordinator.

## Trade-offs

-   **More Complex:** The addition of an extra phase makes 3PC more complex to implement and manage than 2PC.
-   **Still Susceptible to Network Partitions:** While it aims to be non-blocking in coordinator failure, it can still block or lead to inconsistencies under certain network partition scenarios.
-   **Higher Overhead:** The extra communication phase introduces even higher latency and network overhead compared to 2PC.

## Use Case

-   **Systems where blocking is unacceptable:** 3PC is considered in scenarios where the blocking nature of 2PC is deemed too detrimental, and a non-blocking guarantee is highly desired, even at the cost of increased complexity and overhead.
-   **Distributed databases:** Some distributed database systems might implement variations of 3PC to improve availability during coordinator failures, though it is less commonly adopted than 2PC due to its complexity and remaining vulnerabilities.
