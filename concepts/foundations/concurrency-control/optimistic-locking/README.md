# Optimistic Locking

## Core

Optimistic locking is a concurrency control strategy that assumes conflicts between transactions are rare. Instead of preventing conflicts by locking resources, it allows transactions to proceed and checks for conflicts at the time of commit. If a conflict is detected, the transaction is aborted and must be retried. This approach is well-suited for systems with low data contention, as it avoids the overhead of acquiring and releasing locks.

The core idea behind optimistic locking is to use a version identifier, such as a timestamp or a version number, to track changes to data. When a transaction reads an item, it also reads its version. When the transaction attempts to update the item, it checks if the version has changed. If the version is the same, the update is allowed, and the version is incremented. If the version has changed, it means another transaction has modified the data in the meantime, and the current transaction is rolled back.

```mermaid
graph TD
    A[Start Transaction] --> B{Read Data and Version};
    B --> C[Modify Data Locally];
    C --> D{Attempt to Commit};
    D -- Version Matches --> E[Write New Data and Increment Version];
    E --> F[End Transaction (Success)];
    D -- Version Mismatch --> G[Abort Transaction];
    G --> H[Retry Transaction (Optional)];
```

## Characteristics

- **Conflict Detection**: Conflicts are detected at commit time rather than being prevented upfront.
- **Non-Blocking**: Transactions do not block each other during execution, which can improve performance in low-contention environments.
- **Retries**: When a conflict occurs, the application is responsible for retrying the aborted transaction.
- **Versioning**: Relies on version numbers, timestamps, or checksums to detect concurrent modifications.

## Comparison

- **vs. Pessimistic Locking**: Unlike pessimistic locking, which locks resources to prevent conflicts, optimistic locking allows concurrent access and only checks for conflicts at the end. This makes it more performant when conflicts are infrequent.
- **vs. CRDTs**: While both are optimistic approaches, CRDTs (Conflict-free Replicated Data Types) are designed to merge concurrent changes automatically, whereas optimistic locking resolves conflicts by aborting one of the transactions.

## Trade-offs

- **Performance in Low Contention**: Optimistic locking can offer better performance than pessimistic locking in scenarios with few conflicts, as it avoids the overhead of lock management.
- **Starvation**: In high-contention environments, some transactions may be repeatedly aborted and retried, leading to a situation known as starvation, where they never get to complete.
- **Wasted Work**: If a transaction is aborted, all the work it has done is wasted, which can be inefficient for long-running transactions.
- **Complexity**: The application logic must be prepared to handle transaction failures and implement a retry mechanism, which can add complexity.
