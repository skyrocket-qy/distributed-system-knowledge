# Centralized Discovery

## Core

Centralized Discovery is a service discovery pattern where a central server, often referred to as a tracker or bootstrap server, maintains a registry of all active peers or service instances within a distributed system. New peers or clients connect to this central server to obtain a list of other available peers or services they can communicate with.

## Characteristics

- **Centralized Registry**: A single, centralized server or cluster maintains the registry of all service instances.
- **Single Point of Failure**: The central registry can be a single point of of failure.
- **Scalability Bottleneck**: The central registry can become a scalability bottleneck.
- **Simplicity**: Centralized discovery is simpler to implement and manage than decentralized discovery.
- **Control**: It provides a central point for monitoring, managing, and enforcing policies.

## Comparison

| Feature | Description |
|---|---|
| **Architecture** | Centralized server. |
| **Single Point of Failure** | Yes, the central server. |
| **Scalability** | Can be a bottleneck. |
| **Complexity** | Simpler to implement initially. |

## Trade-offs

- **Simplicity vs. Reliability**: Centralized discovery is simpler to implement, but it is less reliable than decentralized discovery.
- **Control vs. Scalability**: Centralized discovery provides more control, but it is less scalable than decentralized discovery.

## How It Works

1.  **Registration:** When a peer or service instance comes online, it registers its network address (e.g., IP address and port) with the central discovery server.
2.  **Heartbeats:** Registered peers periodically send heartbeats to the central server to indicate their liveness and availability. If a peer fails to send heartbeats for a certain period, the central server marks it as offline or removes it from the registry.
3.  **Discovery:** When a new peer or client wants to find other peers or service instances, it queries the central discovery server. The server responds with a list of active and healthy peers.
4.  **Direct Communication:** After obtaining the list of peers, the new peer or client can then establish direct connections with the discovered peers. While the discovery mechanism is centralized, the actual data exchange and communication between peers remain decentralized.

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
