# CAP Theorem



The CAP Theorem, also known as Brewer's theorem, states that it is impossible for a distributed data store to simultaneously provide more than two out of the following three guarantees:

*   **Consistency:** Every read receives the most recent write or an error.
*   **Availability:** Every request receives a (non-error) response, without the guarantee that it contains the most recent write.
*   **Partition Tolerance:** The system continues to operate despite an arbitrary number of messages being dropped (or delayed) by the network between nodes.

## Characteristics

*   **Consistency:** In a consistent system, all nodes see the same data at the same time. When data is written to one node, it is instantly replicated to all other nodes before the write is considered "successful."

*   **Availability:** In an available system, every request made to a node in the system must result in a response. This means that the system is always operational and there are no single points of failure.

*   **Partition Tolerance:** A partition is a communication break between two sets of nodes in a distributed system. Partition tolerance means that the system can sustain any amount of network failure that doesn't result in a failure of the entire network.

## Comparison

In a distributed system, you can only choose two of the three guarantees. This leads to the following trade-offs:

*   **CP (Consistent and Partition Tolerant):** These systems sacrifice availability. In the event of a network partition, the system will shut down the non-consistent part of the system to prevent inconsistencies. Examples include single-master databases like MySQL.

*   **AP (Available and Partition Tolerant):** These systems sacrifice consistency. In the event of a network partition, all nodes remain available, but they may return different versions of the data. Examples include DynamoDB and Cassandra.

*   **CA (Consistent and Available):** These systems sacrifice partition tolerance. This means that they cannot operate in the presence of a network partition and are therefore not suitable for most distributed systems. Traditional relational databases like Oracle and MySQL are examples of CA systems.

## Trade-offs

The CAP theorem forces a trade-off between consistency and availability when a network partition occurs.

*   If you choose **consistency** over availability, the system will return an error or a time-out if it cannot guarantee that the data is up-to-date. This is a good choice for systems that require strong data integrity, such as financial systems.

*   If you choose **availability** over consistency, the system will always return the most recent version of the data it has, which may not be the most recent version in the system. This is a good choice for systems that need to be highly available, such as e-commerce websites.

In modern distributed systems, partition tolerance is a must. Therefore, the trade-off is almost always between consistency and availability.
