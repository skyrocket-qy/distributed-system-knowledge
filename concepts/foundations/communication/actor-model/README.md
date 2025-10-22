# Actor Model

## Core

The **Actor Model** is a powerful and elegant concurrency model that simplifies the design and implementation of concurrent and distributed systems. It treats "actors" as the universal primitives of concurrent computation. Each actor is an independent, isolated entity that encapsulates its own state and behavior, and communicates with other actors exclusively through asynchronous message passing.

### Fundamental Principles

1.  **Actors:** An actor is the fundamental unit of computation. It has:
    *   **State:** Its own private data, which is not directly accessible by other actors.
    *   **Behavior:** Defines how it reacts to messages it receives.
    *   **Mailbox:** A queue where incoming messages are stored until the actor processes them.

2.  **Asynchronous Message Passing:** Actors communicate by sending messages to each other's mailboxes. Message sending is asynchronous and non-blocking; the sender doesn't wait for a response. This promotes loose coupling and allows for high concurrency.

3.  **Isolation:** Actors are completely isolated from each other. They do not share memory or state, eliminating common concurrency issues like race conditions and deadlocks that arise from shared mutable state.

4.  **Supervision:** The Actor Model often includes a hierarchical supervision mechanism. Parent actors supervise their child actors, allowing for robust fault tolerance. If a child actor fails, its supervisor can decide how to handle the failure (e.g., restart the child, escalate the failure).

5.  **Location Transparency:** Actors can be local (running in the same process) or remote (running on a different machine) without requiring changes to the communication logic. This simplifies the transition from concurrent to distributed systems.

### Benefits in Distributed Systems

The Actor Model's principles make it particularly well-suited for distributed environments:

-   **Concurrency:** Asynchronous message passing and isolated state naturally support high levels of concurrency and parallelism.
-   **Fault Tolerance:** The supervision hierarchy allows systems to self-heal and recover from failures gracefully, making them resilient.
-   **Scalability:** Location transparency and message-driven communication facilitate scaling out by distributing actors across multiple nodes.
-   **Responsiveness:** Non-blocking communication ensures that actors can continue processing other messages even when waiting for a response from another actor.

## Comparison

| Feature | Description |
|---|---|
| **Isolation** | Actors encapsulate state and behavior, communicating only via messages. |
| **Concurrency** | Achieved through asynchronous message passing, not shared memory. |
| **Fault Tolerance** | Built-in supervision hierarchies allow for resilient systems. |
| **Location Transparency** | Actors can be local or remote, abstracting distribution. |

## Which service use it?



-   **Erlang/OTP Applications:** Erlang is a programming language built around the Actor Model, and its OTP (Open Telecom Platform) framework is widely used for building highly concurrent, fault-tolerant distributed systems in telecommunications, messaging, and other industries.

-   **Akka Framework (Scala, Java):** Akka provides an implementation of the Actor Model for the JVM, enabling developers to build scalable and resilient concurrent applications in Scala and Java.

-   **Microsoft Orleans (.NET):** Orleans is a framework that implements the Actor Model for building distributed, high-scale computing applications in .NET.

-   **Some Distributed Databases:** Certain distributed databases or data processing systems might use actor-like principles internally for managing concurrency and communication between components.

-   **High-Concurrency Systems:** Any system requiring a high degree of concurrency, fault tolerance, and distributed processing can benefit from the Actor Model, such as real-time analytics, gaming servers, and IoT platforms.



## Related Concepts



-   **Communication:** The Actor Model provides a distinct communication paradigm based on asynchronous message passing, offering an alternative to traditional RPC or shared-memory approaches in distributed systems. [Explore Communication Patterns](../README.md).



-   **Fault Tolerance:** With its inherent supervision hierarchies, the Actor Model offers robust mechanisms for building fault-tolerant systems that can self-heal and recover gracefully from component failures. [Understand Fault Tolerance](../../fault-tolerance/README.md).



-   **Scaling:** The principles of isolation, location transparency, and asynchronous message passing make the Actor Model highly suitable for building scalable distributed systems that can easily expand by adding more actors or nodes. [Learn about Scaling](../../scaling/README.md).



-   **Coordination:** Actors coordinate their activities by exchanging messages, enabling complex distributed logic to be built from simple, independent, and interacting units. [Discover Coordination Concepts](../../coordination/README.md).



-   **Messaging:** The Actor Model's reliance on asynchronous message passing aligns closely with general messaging concepts, providing a structured way to handle inter-component communication in a decoupled manner. [Explore Messaging Systems](../../messaging/README.md).

## Trade-offs
