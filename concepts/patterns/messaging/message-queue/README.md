# Message Queue

## Core

This section describes the Message Queue pattern, where messages are sent to a queue and consumed by a single receiver.

## Comparison

| Feature | Description |
|---|---|
| **Delivery** | One-to-one message delivery. |
| **Decoupling** | High decoupling between sender and receiver. |
| **Asynchronicity** | Asynchronous communication. |
| **Scalability** | Scalable for task distribution and load leveling. |

## Which service use it?

-   **Asynchronous Task Processing:** Sending emails, generating reports, processing images, or performing other time-consuming tasks in the background without blocking the user interface.
-   **Decoupling Microservices:** Allowing different microservices to communicate without direct dependencies, improving resilience and scalability.
-   **Buffering and Load Leveling:** Queues can absorb bursts of requests, protecting backend services from being overwhelmed during peak traffic.
-   **Long-Running Batch Jobs:** Distributing large batch processing tasks across multiple workers, where each worker picks up a message (a unit of work) from the queue.
-   **Order Processing Systems:** Ensuring that orders are processed in a reliable and sequential manner, even if some components are temporarily unavailable.

## Related Concepts

-   **Messaging:** Message Queues are a fundamental messaging pattern that enables one-to-one (point-to-point) communication, providing high decoupling between message producers and consumers. [Explore other Messaging patterns](../README.md).

-   **Publish-Subscribe:** In contrast to Message Queues' one-to-one delivery, Publish-Subscribe offers one-to-many message delivery, where messages are broadcast to multiple interested subscribers. [Compare with Publish-Subscribe](../publish-subscribe/README.md).

-   **Communication:** Message Queues are a key communication paradigm in distributed systems, facilitating asynchronous, reliable, and decoupled interactions between services. [Explore Communication Patterns](../../communication/README.md).

-   **Fault Tolerance:** Message Queues enhance fault tolerance by buffering messages, ensuring that messages are not lost even if consuming services are temporarily unavailable, and enabling retry mechanisms. [Understand Fault Tolerance](../../fault-tolerance/README.md).

-   **Scaling:** Message Queues are crucial for scaling distributed systems by enabling asynchronous task processing, load leveling during traffic spikes, and distributing work efficiently across multiple worker instances. [Learn about Scaling](../../scaling/horizontal/README.md).
