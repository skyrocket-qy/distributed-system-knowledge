# Centralized Discovery

## Core

Centralized Discovery is a service discovery pattern where a central server, often referred to as a tracker or bootstrap server, maintains a registry of all active peers or service instances within a distributed system. New peers or clients connect to this central server to obtain a list of other available peers or services they can communicate with.

## How It Works

1.  **Registration:** When a peer or service instance comes online, it registers its network address (e.g., IP address and port) with the central discovery server.
2.  **Heartbeats:** Registered peers periodically send heartbeats to the central server to indicate their liveness and availability. If a peer fails to send heartbeats for a certain period, the central server marks it as offline or removes it from the registry.
3.  **Discovery:** When a new peer or client wants to find other peers or service instances, it queries the central discovery server. The server responds with a list of active and healthy peers.
4.  **Direct Communication:** After obtaining the list of peers, the new peer or client can then establish direct connections with the discovered peers. While the discovery mechanism is centralized, the actual data exchange and communication between peers remain decentralized.

## Comparison

| Feature | Description |
|---|---|
| **Architecture** | Centralized server. |
| **Single Point of Failure** | Yes, the central server. |
| **Scalability** | Can be a bottleneck. |
| **Complexity** | Simpler to implement initially. |

## Pros

-   **Simplicity:** Easier to implement and manage compared to decentralized discovery mechanisms.
-   **Reliability:** The central server can maintain an accurate and up-to-date list of active peers, as it has a global view of the network.
-   **Control:** Provides a central point for monitoring, managing, and enforcing policies on peer registration and discovery.

## Cons

-   **Single Point of Failure:** The central server is a critical component. If it goes down, new peers cannot join the network, and existing peers might struggle to discover new connections.
-   **Scalability Bottleneck:** The central server can become a performance bottleneck as the number of peers in the network grows, especially if it handles a high volume of registration and discovery requests.
-   **Censorship Vulnerability:** A central server can be a target for censorship or attacks, potentially disrupting the entire network.

## Examples

-   **BitTorrent Trackers:** In older BitTorrent implementations, trackers were central servers that kept track of who had what pieces of a file and helped peers find each other. Modern BitTorrent often uses DHTs for decentralized discovery, but trackers still exist.
-   **Bootstrap Servers:** Many decentralized systems still use a small set of bootstrap nodes or servers to help new nodes join the network for the first time, after which they switch to a decentralized discovery mechanism.

## Related Concepts

-   **Service Discovery:** Centralized discovery is a fundamental pattern within the broader concept of service discovery, providing a central authority for managing and locating service instances. [Explore Service Discovery](../README.MD).

-   **Decentralized Discovery:** In contrast, decentralized discovery mechanisms (e.g., DHTs, gossip protocols) distribute the discovery responsibility across all nodes, aiming to eliminate single points of failure and improve scalability. [Compare with Decentralized Discovery](../decentralized-discovery/README.MD).

-   **Client-Side Service Discovery:** Centralized registries are often queried by client-side discovery mechanisms, where the client directly interacts with the central server to obtain a list of available service instances. [Understand Client-Side Service Discovery](../client-side-discovery/README.MD).

-   **Fault Tolerance:** The primary drawback of centralized discovery is its susceptibility to being a single point of failure, making robust fault tolerance strategies for the central server critical for system reliability. [Learn about Fault Tolerance](../../fault-tolerance/README.MD).

-   **Distributed Consensus:** To overcome the single point of failure issue and ensure high availability and consistency, a centralized service registry itself often employs distributed consensus algorithms internally to replicate its state across multiple nodes. [Understand Distributed Consensus](../../distributed-consensus/README.MD).

## Trade-offs
