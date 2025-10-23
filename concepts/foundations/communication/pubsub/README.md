# Publish-Subscribe (Pub/Sub) Communication

## Core

This section explains the Publish-Subscribe (Pub/Sub) communication pattern, where senders (publishers) broadcast messages to an intermediary, and receivers (subscribers) receive messages they are interested in.

```mermaid
graph TD
    A[Publisher] --> B(Topic);
    B --> C[Subscriber 1];
    B --> D[Subscriber 2];
    B --> E[Subscriber 3];
```


## Characteristics

-   **Asynchronous Communication**: Publishers and subscribers operate independently and do not need to be available at the same time.
-   **Loose Coupling**: Publishers and subscribers are decoupled; publishers do not know who the subscribers are, and subscribers do not know who the publishers are.
-   **Scalability**: The system can be scaled by adding more publishers or subscribers.
-   **Flexibility**: New subscribers can be added without affecting existing publishers.

## Comparison

| Feature | Description |
|---|---|
| **Decoupling** | Publishers and subscribers are highly decoupled. |
| **Asynchronicity** | Communication is typically asynchronous. |
| **Scalability** | Can scale to a large number of publishers and subscribers. |
| **Flexibility** | New subscribers can be added without changing publishers. |

## Trade-offs

| Advantages | Disadvantages |
|---|---|
| **Decoupling**: Publishers and subscribers are decoupled and do not need to know about each other. | **Complexity**: The pub/sub system adds another component to the system, which increases the complexity. |
| **Scalability**: The system can be scaled by adding more publishers or subscribers. | **Message Ordering**: Message ordering is not guaranteed. |
| **Flexibility**: New subscribers can be added without affecting existing publishers. | **Message Delivery**: Message delivery is not guaranteed. |

## Which service use it?



-   **Real-time Data Feeds:** Stock market updates, sports scores, and news feeds often use pub/sub to broadcast information to many interested clients simultaneously.

-   **Event Notifications in Microservices:** When a microservice performs an action (e.g., order placed, user registered), it can publish an event that other services subscribe to and react accordingly.

-   **Chat Applications:** Messages sent in a chat room can be published to a topic, and all participants subscribed to that topic receive the message.

-   **IoT Data Ingestion:** IoT devices can publish sensor readings to topics, and various backend services can subscribe to these topics for processing, analytics, or alerts.

-   **Content Delivery Networks (CDNs):** CDNs can use pub/sub to notify edge locations about content updates or invalidations.
