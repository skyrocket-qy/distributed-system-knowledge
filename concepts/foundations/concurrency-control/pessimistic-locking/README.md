# Pessimistic Locking

## Core

Pessimistic locking is a concurrency control strategy that assumes conflicts between transactions are likely to occur. To prevent conflicts, it locks resources when they are first accessed by a transaction, ensuring that no other transaction can modify them until the lock is released. This approach guarantees that a transaction will not be affected by the activities of other concurrent transactions, providing a high level of isolation.

The most common form of pessimistic locking is two-phase locking (2PL), where a transaction acquires all the locks it needs before it starts releasing any of them. This ensures that once a transaction has completed, its changes are durable and will not be overwritten by other transactions. Pessimistic locking is suitable for environments with high data contention, where the cost of resolving conflicts after they occur would be prohibitive.

## Characteristics

- **Conflict Prevention**: Prevents conflicts by locking resources, ensuring exclusive access.
- **Blocking**: Transactions can be blocked while waiting for a lock to be released, which can lead to performance degradation.
- **Deadlocks**: There is a risk of deadlocks, where two or more transactions are waiting for each other to release locks.
- **Strong Consistency**: Provides strong consistency and isolation guarantees.

## Comparison

- **vs. Optimistic Locking**: In contrast to optimistic locking, which detects conflicts at commit time, pessimistic locking prevents them from happening in the first place. This makes it more suitable for high-contention scenarios.
- **vs. Distributed Locks**: While both involve locking, pessimistic locking is typically associated with database transactions, whereas distributed locks are used to coordinate access to resources across different services or processes in a distributed system.

## Trade-offs

- **Performance in High Contention**: Pessimistic locking can provide better performance than optimistic locking in environments with frequent conflicts, as it avoids the cost of retrying aborted transactions.
- **Reduced Concurrency**: By locking resources, pessimistic locking can limit concurrency, as other transactions may be forced to wait.
- **Deadlock Potential**: The use of locks introduces the possibility of deadlocks, which must be managed through mechanisms like deadlock detection and timeouts.
- **Overhead**: The process of acquiring and releasing locks adds overhead, which can be significant in systems with low contention.
