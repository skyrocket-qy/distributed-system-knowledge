# Scalability

## Core

Scalability is the property of a system to handle a growing amount of work by adding resources to the system. In the context of distributed systems, scalability is crucial for ensuring that the system can accommodate increasing numbers of users, data, or transactions without a significant degradation in performance.

There are two primary ways to scale a system:

*   **Vertical Scaling (Scaling Up):** This involves adding more resources (e.g., CPU, RAM) to a single node. It's a straightforward approach but has limitations, as there is a physical limit to the resources that can be added to a single machine.
*   **Horizontal Scaling (Scaling Out):** This involves adding more nodes to the system. This is the more common approach in distributed systems, as it allows for virtually limitless scaling.

## Characteristics

-   **Performance:** A scalable system should be able to maintain or improve its performance as the load increases.
-   **Elasticity:** The ability to add or remove resources on-demand to match the current workload.
-   **Reliability:** A scalable system should also be reliable, as adding more components can increase the probability of failures.

## Comparison

| Feature            | Vertical Scaling (Scaling Up)          | Horizontal Scaling (Scaling Out)       |
| ------------------ | -------------------------------------- | -------------------------------------- |
| **Resource**       | Add more resources (CPU, RAM) to a single node. | Add more nodes to the system.          |
| **Complexity**     | Relatively simple to implement.        | More complex, requires load balancing and coordination. |
| **Cost**           | Can be expensive due to high-end hardware. | Can be more cost-effective with commodity hardware. |
| **Limitations**    | Limited by the capacity of a single machine. | Can scale to a much larger extent.     |

## Trade-offs

### Vertical Scaling

*   **Advantages:** Simpler to manage, no need for complex coordination between nodes.
*   **Disadvantages:** Single point of failure, limited scalability, higher cost for high-end hardware.

### Horizontal Scaling

*   **Advantages:** High scalability, improved fault tolerance, cost-effective.
*   **Disadvantages:** Increased complexity in managing multiple nodes, requires load balancing and service discovery.

