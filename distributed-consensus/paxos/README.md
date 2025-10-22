# Paxos

## Core

**Paxos** is a family of protocols for solving the distributed consensus problem in an asynchronous network prone to failures (including crash failures of processes and message loss, duplication, or reordering). Its primary goal is to ensure that all non-faulty processes agree on a single value, even if some processes fail or messages are lost. Paxos is renowned for its correctness and resilience but is also known for its complexity.

### Key Concepts

-   **Proposer:** Proposes a value to be chosen.
-   **Acceptor:** Votes on proposals and accepts chosen values.
-   **Learner:** Learns the chosen value.
-   **Phases:** The protocol typically involves two phases: Prepare and Accept.

### Key Challenges

-   **Complexity:** Paxos is notoriously difficult to understand and implement correctly.
-   **Liveness:** While ensuring safety (agreement on a single value), basic Paxos does not guarantee liveness (that a value will eventually be chosen) without additional mechanisms (e.g., leader election).

## How It Works (Simplified Two-Phase Paxos)

1.  **Phase 1 (Prepare):**
    *   A Proposer chooses a new proposal number `n` (higher than any it has seen before) and sends a `prepare` message to a majority of Acceptors.
    *   An Acceptor, upon receiving a `prepare(n)` message, if `n` is greater than any proposal number it has already responded to, promises not to accept any more proposals with a number less than `n`. It also responds with the proposal number and value of the highest-numbered proposal it has accepted (if any).

2.  **Phase 2 (Accept):**
    *   If the Proposer receives responses from a majority of Acceptors, it examines the responses. If any Acceptor reported a previously accepted value, the Proposer must propose that value. Otherwise, it can propose its own value `v`.
    *   The Proposer then sends an `accept(n, v)` message to the same majority of Acceptors.
    *   An Acceptor, upon receiving an `accept(n, v)` message, accepts the proposal if it has not promised to ignore proposals with a number less than `n`. It then records `(n, v)` as its accepted proposal.

## Which service use it?

-   **Google Chubby:** A distributed lock service that uses Paxos to maintain consistency.
-   **Google Spanner:** A globally distributed database that uses Paxos for strong consistency across replicas.
-   **Apache ZooKeeper (ZAB protocol):** While not pure Paxos, ZooKeeper's ZAB (ZooKeeper Atomic Broadcast) protocol is inspired by Paxos and is used for distributed coordination and leader election.

## Related Concepts

-   **Distributed Consensus:** Paxos is one of the foundational algorithms for solving the distributed consensus problem. [Explore Distributed Consensus](../README.md).
-   **Leader Election:** Paxos often requires a leader election mechanism to ensure liveness and make progress. [Understand Leader Election](../../coordination/leader-election/README.md).
-   **Strong Consistency:** Paxos is used to achieve strong consistency in distributed systems by ensuring all replicas agree on the order of operations. [Learn about Strong Consistency](../../consistency-models/strong-consistency/README.md).
-   **Fault Tolerance:** Paxos is designed to tolerate crash failures of nodes and message loss, making it a key component in building fault-tolerant systems. [Understand Fault Tolerance](../../fault-tolerance/README.md).
-   **Raft:** A more understandable alternative to Paxos for achieving distributed consensus. [Compare with Raft](./raft/README.md).
