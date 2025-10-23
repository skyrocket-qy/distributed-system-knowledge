# Publish-Subscribe

## Core

This section describes the Publish-Subscribe pattern, where messages are published to a topic and received by multiple subscribers.

## Characteristics

- **One-to-many Delivery**: Each message is delivered to multiple subscribers.
- **Asynchronous**: Publishers and subscribers are decoupled and communicate asynchronously.
- **Decoupling**: Publishers and subscribers are decoupled and do not need to know about each other.
- **Scalability**: Publish-subscribe systems can be scaled to handle a large number of publishers and subscribers.
- **Flexibility**: New subscribers can be added without affecting existing publishers.

## Comparison

| Feature | Description |
|---|---|
| **Delivery** | One-to-many message delivery. |
| **Decoupling** | High decoupling between publisher and subscribers. |
| **Asynchronicity** | Asynchronous communication. |
| **Scalability** | Scalable for broadcasting events to many consumers. |

## Trade-offs

- **Performance vs. Reliability**: Higher reliability guarantees can come at the cost of lower performance.
- **Complexity vs. Flexibility**: More flexible messaging patterns can be more complex to manage.

## Which service use it?

-   **Real-time Data Feeds:** Stock market updates, sports scores, and news feeds often use pub/sub to broadcast information to many interested clients simultaneously.
-   **Event Notifications in Microservices:** When a microservice performs an action (e.g., order placed, user registered), it can publish an event that other services subscribe to and react accordingly.
-   **Chat Applications:** Messages sent in a chat room can be published to a topic, and all participants subscribed to that topic receive the message.
-   **IoT Data Ingestion:** IoT devices can publish sensor readings to topics, and various backend services can subscribe to these topics for processing, analytics, or alerts.
-   **Content Delivery Networks (CDNs):** CDNs can use pub/sub to notify edge locations about content updates or invalidations.
