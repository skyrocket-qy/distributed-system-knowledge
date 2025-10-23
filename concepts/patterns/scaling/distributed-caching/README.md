# Distributed Caching

## Core

**Distributed Caching** involves storing frequently accessed data across multiple servers in a distributed system. The primary goal is to improve application performance by reducing the latency of data retrieval and decreasing the load on backend data stores (like databases). Instead of fetching data from a slower, persistent storage every time, applications can retrieve it quickly from an in-memory cache.

### Key Challenges

-   **Cache Coherency:** Ensuring that all cached copies of data are consistent with the source of truth, especially when data is updated. This is a significant challenge in distributed environments.
-   **Cache Invalidation:** Determining when cached data is stale and needs to be removed or updated. Strategies include Time-To-Live (TTL), explicit invalidation, or write-through/write-back policies.
-   **Data Partitioning/Sharding:** How cached data is distributed across multiple cache nodes to handle large datasets and high request volumes.
-   **Fault Tolerance:** Ensuring the cache remains available and data is not lost if a cache node fails.
-   **Network Overhead:** The overhead of communicating with cache servers, though typically much lower than communicating with a database.

## Characteristics

- **Performance**: Distributed caching can significantly improve the performance of a system by reducing the latency of data access.
- **Scalability**: Distributed caching can improve the scalability of a system by reducing the load on the backend data store.
- **Availability**: Distributed caching can improve the availability of a system by providing a fallback in case the backend data store is unavailable.
- **Consistency**: Distributed caching can introduce consistency issues, as the cached data may not be up-to-date.
- **Cost**: Distributed caching can be expensive to implement and maintain.

## Comparison

| Caching Strategy | Write Latency | Data Consistency |
|---|---|---|
| **Cache-Aside** | High | Eventual |
| **Write-Through** | High | Strong |
| **Write-Back** | Low | Eventual |

## Trade-offs

- **Performance vs. Consistency**: Caching can improve performance, but it can also introduce consistency issues.
- **Cost vs. Performance**: Caching can be expensive, but it can also significantly improve performance.

## Types of Distributed Caching Architectures

-   **Client-Side Caching:** Each client maintains its own cache. Simple but can lead to stale data if not managed carefully.
-   **Server-Side Caching (Dedicated Cache Servers):** Data is stored in a cluster of dedicated cache servers (e.g., Redis, Memcached). Clients connect to these servers to store and retrieve data.
-   **CDN (Content Delivery Network):** A geographically distributed network of proxy servers and their data centers. The goal is to provide high availability and performance by distributing the service spatially relative to end-users.

## Implementation Strategies

-   **Cache-Aside (Lazy Loading):** The application is responsible for checking the cache first. If data is not found (cache miss), it fetches from the database, stores it in the cache, and then returns it. This is the most common strategy.
-   **Write-Through:** Data is written to the cache and the database simultaneously. This ensures data consistency but can add latency to write operations.
-   **Write-Back (Write-Behind):** Data is written to the cache first, and the cache asynchronously writes the data to the database. This offers low write latency but risks data loss if the cache fails before data is persisted.

## Which service use it?

-   **Web Applications:** To cache frequently accessed web pages, user sessions, and API responses, significantly improving response times.
-   **E-commerce Platforms:** Caching product catalogs, user profiles, and shopping cart data.
-   **Gaming:** Storing game state, leaderboards, and user data for quick access.
-   **Real-time Analytics:** Caching aggregated results or frequently queried data to speed up dashboards and reports.
