# Concurrency Control

## Core

Concurrency control in distributed systems refers to the mechanisms used to ensure that concurrent operations on shared data do not violate the data's correctness. It addresses the challenges that arise when multiple transactions or processes access and modify the same data simultaneously. Without effective concurrency control, systems can suffer from data corruption, inconsistencies, and race conditions, leading to unreliable behavior.

The primary goal of concurrency control is to manage the execution of concurrent operations in a way that maintains data integrity while maximizing system performance. This involves preventing undesirable phenomena such as lost updates, dirty reads, and non-repeatable reads. By coordinating access to shared resources, concurrency control protocols ensure that the system behaves as if all operations were executed in a sequential, well-defined order.

## Key Challenges

- **Isolation**: Concurrency control mechanisms provide isolation, which ensures that each transaction appears to execute in isolation from others. This is one of the key properties of ACID (Atomicity, Consistency, Isolation, Durability).
- **Correctness**: They maintain the correctness of data by preventing race conditions and conflicts that could lead to inconsistencies.
- **Performance**: The choice of concurrency control strategy can significantly impact system performance, affecting throughput and latency.
- **Scalability**: Effective concurrency control is essential for building scalable systems that can handle a high volume of concurrent requests.

## Comparison

Concurrency control strategies are broadly categorized into two main approaches:

| Approach | Mechanism | When Conflicts Detected | Performance Impact | Use Case |
|---|---|---|---|---|
| **[Optimistic Locking](./optimistic-locking)** | Allows concurrent transactions to proceed without locks, assuming conflicts are rare. Conflicts are detected at commit time. | At commit time | Lower overhead for low contention; higher overhead for high contention (rollbacks) | High-read, low-write workloads; web applications; collaborative editing | 
| **[Pessimistic Locking](./pessimistic-locking)** | Prevents conflicts by acquiring locks on resources before accessing them. Transactions wait for locks to be released. | Before access (prevented) | Higher overhead due to locking; potential for deadlocks | High-contention environments; critical financial transactions; resource-intensive operations |