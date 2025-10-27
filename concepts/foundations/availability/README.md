# Availability



Availability is a measure of the time that a system is operational and accessible to its users. In distributed systems, high availability is a key requirement, as it ensures that the system can continue to function even in the event of node failures or network partitions.

Availability is often expressed as a percentage of uptime over a given period. For example, a system with 99.9% availability will be down for no more than 8.76 hours per year.

## Characteristics

-   **Fault Tolerance:** The ability of a system to continue operating in the event of failures.
-   **Redundancy:** Having multiple copies of a component to take over in case one fails.
-   **Monitoring:** Continuously monitoring the system for failures and performance degradation.

## Comparison

| Approach             | Description                                          | Use Case                                           |
| -------------------- | ---------------------------------------------------- | -------------------------------------------------- |
| **Active-Passive**   | One node is active, and the other is on standby.     | A simple, cost-effective high-availability solution. |
| **Active-Active**    | All nodes are active and share the workload.         | A more complex but highly available and scalable solution. |

## Trade-offs

*   **Availability vs. Consistency:** In some distributed systems, high availability can come at the cost of strong consistency, as described by the CAP theorem.
*   **Cost:** Achieving high availability often requires additional hardware and software, which can increase costs.
*   **Complexity:** High-availability solutions can be complex to design, implement, and manage.
