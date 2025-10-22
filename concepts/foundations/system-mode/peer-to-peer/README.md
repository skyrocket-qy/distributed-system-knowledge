# Peer-to-Peer (P2P) Mode

## Core

A **Peer-to-Peer (P2P)** system mode is a decentralized architectural model where all participating nodes, called peers, have equivalent capabilities and responsibilities. Unlike the client-server model, there is no central server. Peers communicate directly with each other to share resources, workloads, and data.

Each peer can act as both a client (requesting services) and a server (providing services). This creates a resilient and scalable network where the failure of a single peer does not bring down the entire system.

## Characteristics

- **Decentralization**: There is no central server; all nodes are equal.
- **Scalability**: The system scales as more peers join the network.
- **Resilience**: The system is resilient to the failure of individual nodes.
- **Autonomy**: Each peer is autonomous and can control its own resources.
- **Self-organization**: The network can organize itself without a central coordinator.

## Comparison

| Feature | Peer-to-Peer | Client-Server |
|---|---|---|
| **Architecture** | Decentralized | Centralized |
| **Scalability** | High | Low |
| **Resilience** | High | Low |
| **Complexity** | High | Low |

## Trade-offs

- **Scalability**: The system scales as more peers join the network.
- **Resilience**: The system is resilient to the failure of individual nodes.
- **Complexity**: P2P networks can be complex to design and manage.
- **Security**: P2P networks can be vulnerable to security threats.
- **Availability**: Data is only available if the peers storing it are online.

## How It Works

In a P2P network, peers need a way to discover each other. This can be done in several ways:
-   **[Centralized Discovery](../../service-discovery/centralized-discovery/README.md):** A central server (a tracker or bootstrap server) maintains a list of active peers. New peers connect to this server to get a list of other peers they can connect to. While discovery is centralized, the actual data exchange is P2P.
-   **[Decentralized Discovery](../../service-discovery/decentralized-discovery/README.md):** Peers discover each other using protocols like Distributed Hash Tables (DHTs). In a DHT, each peer is responsible for storing a small portion of the routing information, creating a decentralized index for the entire network.

Once connected, peers can exchange information directly. For example, in a file-sharing application, a peer can download parts of a file from multiple other peers simultaneously, increasing download speed.

P2P networks can be:
-   **Unstructured:** Peers connect to each other in an ad-hoc manner. Finding specific data can be inefficient as requests may need to be flooded across the network.
-   **Structured:** Peers are organized in a specific topology (e.g., a ring or a tree), and data is placed at specific locations, making searches very efficient. DHTs are an example of structured P2P networks.

## Pros & Cons

### Pros

-   **Scalability:** The total capacity of the system increases as more peers join the network, since each peer adds new resources.
-   **Resilience and Fault Tolerance:** There is no single point of failure. The system can continue to operate even if some peers go offline.
-   **Cost-Effectiveness:** P2P networks do not require powerful and expensive central servers, reducing infrastructure costs.
-   **Censorship Resistance:** The decentralized nature makes it difficult for any central authority to shut down or censor the system.

### Cons

-   **Discovery and Coordination:** Finding peers and coordinating their actions can be complex without a central server.
-   **Data Availability:** Data is only available if the peers storing it are online. If all peers with a piece of data go offline, that data becomes inaccessible.
-   **Security:** P2P networks can be vulnerable to security threats such as malicious peers, data poisoning, and denial-of-service attacks.
-   **Inconsistent Performance:** The performance of the network can be unpredictable and depends on the number of peers online and their network conditions.

## Which service use it?

-   **File Sharing Networks (e.g., BitTorrent):** Users directly share files with each other without a central server mediating the transfers.
-   **Cryptocurrencies (e.g., Bitcoin, Ethereum):** The blockchain is maintained and validated by a decentralized network of peer nodes, where each node holds a copy of the ledger and participates in transaction verification.
-   **Distributed Content Delivery Networks (CDNs):** Some CDNs use P2P principles to distribute content more efficiently, allowing users to download content from nearby peers.
-   **Some Online Gaming Platforms:** Certain games use P2P connections for direct communication between players, especially for real-time multiplayer experiences.

## Related Concepts

-   **System Modes:** Peer-to-Peer (P2P) is a fundamental decentralized system mode that contrasts with centralized client-server architectures, distributing responsibilities and resources across all participating nodes. [Explore other System Modes](../README.md).

-   **Peer-to-Peer Communication:** The P2P system mode is intrinsically linked to peer-to-peer communication, where nodes directly exchange data and messages without relying on a central intermediary. [Learn more about Peer-to-Peer Communication](../../communication/p2p/README.md).

-   **Fault Tolerance:** P2P systems are inherently fault-tolerant due to their decentralized nature; the absence or failure of individual nodes does not typically lead to a complete system outage, enhancing overall resilience. [Understand Fault Tolerance](../../fault-tolerance/README.md).

-   **Scaling:** P2P architectures offer high scalability, as the system's capacity often increases with the addition of more peers, each contributing resources and bandwidth to the network. [Learn about Scaling](../../scaling/README.md).

-   **Distributed Consensus:** Many prominent P2P applications, such as cryptocurrencies, rely on sophisticated distributed consensus algorithms to maintain a consistent and agreed-upon state across the decentralized network. [Understand Distributed Consensus](../../distributed-consensus/README.md).

-   **Topology:** P2P networks can adopt various topologies (e.g., mesh, ring, star) to organize their connections and facilitate communication and discovery among peers, each with its own trade-offs in performance and resilience. [Explore Network Topologies](../../topology/README.md).
