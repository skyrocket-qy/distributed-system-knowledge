# Server-Side Service Discovery

## Core

Server-Side Service Discovery is a pattern where clients make requests to a service via a router, load balancer, or API Gateway. This intermediary is responsible for querying the service registry to find available service instances and then forwarding the client's request to one of them. The client itself does not need to know about the service registry or the specific network locations of service instances.

## Characteristics

- **Server-side Logic**: The server-side component (e.g., load balancer) is responsible for querying the service registry and load balancing.
- **Simplified Client**: The client is simpler, as it does not need to handle service discovery logic.
- **Centralized Control**: The server-side component can provide centralized control over routing and load balancing.
- **Single Point of Failure**: The server-side component can be a single point of failure.
- **Latency**: The server-side component can introduce an additional network hop, which can increase latency.

## Comparison

| Feature | Server-Side Discovery | Client-Side Discovery |
|---|---|---|
| **Client Complexity** | Low | High |
| **Infrastructure Complexity** | High | Low |
| **Centralized Control** | Yes | No |
| **Latency** | High | Low |

## Trade-offs

- **Simplicity vs. Flexibility**: Server-side service discovery simplifies the client, but it is less flexible than client-side service discovery.
- **Performance vs. Reliability**: The server-side component can be a single point of failure, but it can also provide centralized control and improve reliability.

## How It Works

1.  **Service Registration:** Similar to client-side discovery, service instances register their network locations with a service registry upon startup and send heartbeats to maintain their status.
2.  **Service Deregistration:** Service instances deregister upon shutdown, or are removed by the registry if heartbeats cease.
3.  **Client Request:** A client application sends a request to a well-known address of a router, load balancer, or API Gateway.
4.  **Intermediary Query:** The intermediary (router/load balancer/API Gateway) queries the service registry to get a list of available instances for the requested service.
5.  **Request Forwarding:** The intermediary then selects a healthy service instance (using its own load-balancing logic) and forwards the client's request to that instance.

## Key Components

-   **Service Registry:** Stores the locations and health status of service instances (e.g., Kubernetes DNS, AWS Cloud Map).
-   **Router/Load Balancer/API Gateway:** An intermediary that intercepts client requests, performs service discovery, and forwards requests (e.g., Nginx, HAProxy, AWS Elastic Load Balancer, Kubernetes Kube-proxy).

## Pros

-   **Client Simplicity:** Clients are simpler as they don't need to implement any service discovery logic. They just send requests to a fixed endpoint.
-   **Language Agnostic:** Works with clients written in any language, as the discovery logic is handled by the intermediary.
-   **Centralized Control:** The intermediary can enforce policies, perform centralized logging, and apply security measures.

## Cons

-   **Infrastructure Complexity:** Requires deploying and managing an additional infrastructure component (the intermediary) which can become a single point of failure if not properly configured for high availability.
-   **Potential Performance Bottleneck:** The intermediary can become a bottleneck if not scaled appropriately to handle the request load.
-   **Additional Hop:** Introduces an extra network hop for every request, potentially increasing latency.

## Examples

-   **AWS Elastic Load Balancer (ELB):** A managed load balancing service that distributes incoming application traffic across multiple targets, such as EC2 instances, in multiple Availability Zones.
-   **Kubernetes Services:** Kubernetes uses its own DNS-based service discovery where services are exposed via stable IP addresses and DNS names, and `kube-proxy` handles the forwarding of requests to pods.
-   **Nginx/HAProxy with Service Discovery Integration:** These can be configured to dynamically discover backend services by integrating with service registries like Consul or Eureka.

## Related Concepts

-   **Service Discovery:** Server-side service discovery is a fundamental pattern within the broader concept of service discovery, where an intermediary handles the logic of locating and routing requests to service instances. [Explore Service Discovery](../README.md).

-   **Client-Side Service Discovery:** In contrast, client-side service discovery places the responsibility of querying the service registry and load-balancing directly on the client application, leading to simpler infrastructure but more complex clients. [Compare with Client-Side Service Discovery](../client-side-discovery/README.md).

-   **Communication:** Server-side service discovery acts as a crucial layer for inter-service communication, abstracting away the dynamic network locations of services from the clients and routing requests efficiently. [Understand Communication Patterns](../../communication/README.md).

-   **Horizontal Scaling:** Server-side service discovery is particularly effective in horizontally scaled environments, as the intermediary can dynamically adapt to a fluctuating number of service instances and distribute load across them. [Learn about Horizontal Scaling](../../scaling/horizontal/README.md).

-   **Fault Tolerance:** The intermediary (router/load balancer) in server-side discovery must be highly available and fault-tolerant itself to avoid becoming a single point of failure, and it contributes to overall system fault tolerance by routing requests away from unhealthy service instances. [Understand Fault Tolerance](../../fault-tolerance/README.md).

-   **Microservices Architecture (System Mode):** Server-side service discovery is a common and often preferred pattern in microservices architectures, simplifying client implementations and providing centralized control over traffic management and routing. [Discover System Modes](../../system-mode/README.md).
