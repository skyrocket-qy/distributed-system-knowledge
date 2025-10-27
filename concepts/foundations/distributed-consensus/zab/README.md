# ZAB (ZooKeeper Atomic Broadcast)



The ZAB (ZooKeeper Atomic Broadcast) protocol is a consensus protocol that underpins Apache ZooKeeper, ensuring strong consistency and fault tolerance in distributed systems. It is designed to maintain a consistent state across all nodes in a ZooKeeper ensemble, even in the presence of failures or network partitions. ZAB ensures that all nodes process transactions in the exact same order, guaranteeing sequential consistency.

## Characteristics

-   **Total Order Broadcast:** All nodes process transactions in the same order.
-   **Fault Tolerance:** Continues operation despite individual node failures.
-   **High Availability:** Quickly elects a new leader during failures.
-   **State Synchronization:** Ensures all servers converge on the same state during recovery and normal operation.

## Phases

1.  **Leader Election:** When a ZooKeeper ensemble starts or if the current leader fails, nodes elect a new leader. The node with the most up-to-date state is typically chosen.
2.  **Discovery and Synchronization:** The elected leader gathers information about recent transactions from followers and synchronizes their states, proposing any missing transactions.
3.  **Atomic Broadcast (Normal Operation):** All write requests go to the leader. The leader proposes transactions, broadcasts them to followers, and once a quorum of followers acknowledges, the leader commits the transaction and informs followers to do the same.

## Use Cases

-   **Apache ZooKeeper:** ZAB is the core protocol used by Apache ZooKeeper for distributed coordination, configuration management, naming, and providing distributed synchronization.

