# Load Balancing



**Load balancing** is the process of distributing incoming network traffic across multiple servers to ensure that no single server is overwhelmed. By spreading the load, load balancing improves responsiveness and increases the availability of applications.

## Characteristics

- **Scalability**: Load balancing can improve the scalability of a system by distributing the load across multiple servers.
- **Availability**: Load balancing can improve the availability of a system by redirecting traffic away from failed servers.
- **Performance**: Load balancing can improve the performance of a system by reducing the response time.
- **Flexibility**: Load balancing can provide flexibility in adding and removing servers from the pool.
- **Complexity**: Load balancing can add complexity to a system.

## Comparison

| Type | How it works | Use Case |
|---|---|---|
| **Round Robin** | Distributes requests sequentially to a group of servers. | Simple, effective for servers with similar capacity. |
| **Least Connections** | Sends traffic to the server with the fewest active connections. | Effective when requests have varying completion times. |
| **IP Hash** | The IP address of the client is used to determine which server receives the request. | Ensures a user is consistently sent to the same server. |

## Trade-offs

| Type | Advantages | Disadvantages |
|---|---|---|
| **Round Robin** | Simple to implement. | Does not account for server load or capacity. |
| **Least Connections** | Adapts to server load. | Can be more complex to implement. |
| **IP Hash** | Sticky sessions. | Can lead to uneven load distribution. |
