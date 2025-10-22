# Distributed Systems Concepts

## Introduction

A distributed system is a collection of independent computers that appears to its users as a single coherent system. These systems are designed to solve problems that are too large or complex for a single machine, offering advantages such as enhanced scalability, reliability, and fault tolerance.

This repository explores the fundamental concepts, patterns, and infrastructure of distributed systems.

## Concepts

### Foundations

-   **[Communication](./concepts/foundations/communication/README.md):** The exchange of information between processes on different nodes.
-   **[Conflict Resolution](./concepts/foundations/conflict-resolution/README.md):** Managing inconsistencies that arise from concurrent updates.
-   **[Consistency Models](./concepts/foundations/consistency-models/README.md):** Guarantees about the visibility and ordering of updates.
-   **[Coordination](./concepts/foundations/coordination/README.md):** Managing interactions and dependencies between processes.
-   **[Distributed Consensus](./concepts/foundations/distributed-consensus/README.md):** Reaching agreement among a group of nodes.
-   **[Distributed Transactions](./concepts/foundations/distributed-transactions/README.md):** Ensuring atomicity and consistency across multiple nodes.
-   **[Fault Tolerance](./concepts/foundations/fault-tolerance/README.md):** The ability of a system to continue operating in the event of failures.
-   **[Security](./concepts/foundations/security/README.md):** Protecting the system from unauthorized access and malicious attacks.
-   **[System Modes](./concepts/foundations/system-mode/README.md):** The different operational states of a distributed system.
-   **[Topology](./concepts/foundations/topology/README.md):** The arrangement of nodes and connections in a network.

### Patterns

-   **[Data Replication](./concepts/patterns/data-replication/README.md):** Creating and maintaining multiple copies of data on different nodes.
-   **[Messaging](./concepts/patterns/messaging/README.md):** Asynchronous communication between processes.
-   **[Observability](./concepts/patterns/observability/README.md):** Gaining insights into the behavior of a system.
-   **[Scaling](./concepts/patterns/scaling/README.md):** Increasing the capacity of a system to handle more load.
-   **[Service Discovery](./concepts/patterns/service-discovery/README.md):** The process of automatically detecting devices and services on a network.

### Infrastructure

-   **[Caching](./concepts/infrastructure/caching/README.md):** Storing data in a temporary location for faster access.
-   **[Load Balancing](./concepts/infrastructure/load-balancing/README.md):** Distributing traffic across multiple servers.
-   **[Proxies](./concepts/infrastructure/proxies/README.md):** Intermediary servers that forward requests between clients and servers.

## Resources

-   **[Contributing](./CONTRIBUTING.md):** Guidelines for contributing to this project.
-   **[Glossary](./GLOSSARY.md):** Definitions of common terms in distributed systems.

## Further Reading

-   [What is a distributed system?](https://www.atlassian.com/microservices/microservices-architecture/distributed-architecture)
-   [Distributed Systems: An Introduction](https://www.confluent.io/learn/distributed-systems/)
-   [What Are Distributed Systems?](https://www.splunk.com/en_us/blog/learn/distributed-systems.html)
