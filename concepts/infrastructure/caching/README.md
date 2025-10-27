# Caching



**Caching** is the process of storing copies of files or data in a temporary storage location, or "cache," so that they can be accessed more quickly. Caching is used to reduce latency and improve the performance of systems by serving data from the cache instead of fetching it from the original source.

## Characteristics

- **Performance**: Caching can significantly improve the performance of a system by reducing the latency of data access.
- **Scalability**: Caching can improve the scalability of a system by reducing the load on the backend data store.
- **Availability**: Caching can improve the availability of a system by providing a fallback in case the backend data store is unavailable.
- **Consistency**: Caching can introduce consistency issues, as the cached data may not be up-to-date.
- **Cost**: Caching can be expensive to implement and maintain.

## Comparison

| Type | How it works | Use Case |
|---|---|---|
| **In-memory Cache** | Stores data in RAM for very fast access. | Caching frequently accessed data. |
| **Distributed Cache** | Pools the RAM of multiple computers to create a single cache. | Scaling the cache across multiple servers. |
| **Content Delivery Network (CDN)** | Caches content in multiple locations around the world. | Caching static content closer to users. |

## Trade-offs

| Type | Advantages | Disadvantages |
|---|---|---|
| **In-memory Cache** | Extremely fast. | Limited by the amount of RAM on a single server. |
| **Distributed Cache** | Scalable and resilient. | More complex to manage. |
| **Content Delivery Network (CDN)** | Low latency for users. | Can be expensive. |
