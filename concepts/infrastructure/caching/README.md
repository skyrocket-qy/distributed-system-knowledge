# Caching

## Core

**Caching** is the process of storing copies of files or data in a temporary storage location, or "cache," so that they can be accessed more quickly. Caching is used to reduce latency and improve the performance of systems by serving data from the cache instead of fetching it from the original source.

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
