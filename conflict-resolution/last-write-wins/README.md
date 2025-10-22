# Last Write Wins (LWW) for Conflict Resolution

## Core

This section describes the Last Write Wins (LWW) strategy for conflict resolution, where the most recent write operation (based on a timestamp) is chosen as the definitive version, discarding older conflicting writes.

## Comparison

| Feature | Description |
|---|---|
| **Simplicity** | Easy to implement and understand. |
| **Data Loss** | Potential for data loss if an older, semantically important write is overwritten. |
| **Performance** | Generally high, as it avoids complex merge logic. |
| **Dependency** | Relies on accurate timestamps across distributed nodes. |

## Which service use it?



-   **Eventually Consistent Key-Value Stores:** Many NoSQL databases that prioritize availability and partition tolerance (e.g., some configurations of Apache Cassandra, Amazon DynamoDB) use LWW as a default or configurable conflict resolution strategy.

-   **Caching Systems:** When multiple clients update the same cached item, the last update often overwrites previous ones, especially in distributed caches.

-   **Simple Data Synchronization:** In scenarios where data loss from concurrent updates is acceptable or rare, and a simple resolution mechanism is preferred, LWW can be used.

-   **Session Management:** In distributed web applications, if multiple requests update a user's session data concurrently, LWW might be used to ensure the most recent session state is preserved.
