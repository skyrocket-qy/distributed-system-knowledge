# Checkpointing

## Core

This section explains Checkpointing as a fault-tolerance technique, involving periodically saving the state of a distributed computation to stable storage to enable rollback recovery.

## Comparison

| Feature | Description |
|---|---|
| **Recovery** | Enables rollback recovery to a previous consistent state. |
| **Overhead** | Introduces overhead due to state saving. |
| **Recovery Time** | Depends on the frequency of checkpoints and state size. |
| **Data Loss** | Minimal data loss, up to the last checkpoint. |

## Which service use it?



-   **Long-Running Batch Processing Jobs (e.g., Apache Spark, Apache Flink):** These frameworks periodically save the state of computations, allowing them to resume from the last successful checkpoint if a worker node fails, rather than restarting the entire job.

-   **Scientific Simulations:** Complex and time-consuming scientific simulations often use checkpointing to save their progress, enabling recovery from system crashes or allowing the simulation to be paused and resumed later.

-   **Stateful Stream Processing Applications:** Stream processing engines (e.g., Apache Flink, Apache Kafka Streams) use checkpointing to persist the state of their operators, ensuring fault tolerance and exactly-once processing guarantees.

-   **Distributed Databases:** Some distributed databases use checkpointing internally to periodically flush in-memory changes to disk, reducing recovery time after a crash.

-   **Virtual Machine (VM) Snapshots:** While not exactly the same, the concept of taking a snapshot of a running VM's state is analogous to checkpointing, allowing the VM to be restored to a previous point in time.

## Related Concepts

-   **Fault Tolerance:** Checkpointing is a fundamental fault tolerance technique that enables distributed systems to recover from failures by rolling back to a previously saved consistent state, minimizing data loss and downtime. [Explore other Fault Tolerance strategies](../README.md).

-   **Snapshot Recovery:** Checkpointing is closely related to snapshot recovery, where a complete state of a system or component is captured at a specific point in time for later restoration. Checkpointing often refers to more granular, periodic state saving. [Compare with Snapshot Recovery](../snapshot/README.md).

-   **Data Replication:** Checkpointing can be used in conjunction with data replication to ensure that replicated data can be consistently recovered across all nodes, especially in stateful distributed applications. [Understand Data Replication](../../data-replication/README.md).

-   **Consistency Models:** Achieving consistent checkpoints in a distributed system requires careful consideration of consistency models to ensure that the saved state accurately reflects a valid global state of the system, avoiding inconsistencies upon recovery. [Learn about Consistency Models](../../consistency-models/README.md).
