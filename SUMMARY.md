# Learning Roadmap: Distributed Systems Concepts

This roadmap is designed to guide you through the fundamental concepts of distributed systems in a logical learning order. Each section builds upon the previous one, providing a structured path to understanding.

*   [Introduction](README.md)

## Foundations

*   [Availability](concepts/foundations/availability/README.md)
*   [CAP Theorem](concepts/foundations/cap-theorem/README.md)
*   [Consistency Models](concepts/foundations/consistency-models/README.md)
    *   [Causal Consistency](concepts/foundations/consistency-models/causal-consistency/README.md)
    *   [Eventual Consistency](concepts/foundations/consistency-models/eventual-consistency/README.md)
    *   [Sequential Consistency](concepts/foundations/consistency-models/sequential/README.md)
    *   [Strong Consistency](concepts/foundations/consistency-models/strong-consistency/README.md)
*   [Communication](concepts/foundations/communication/README.md)
    *   [Client-Server](concepts/foundations/communication/client-server/README.md)
    *   [P2P](concepts/foundations/communication/p2p/README.md)
    *   [Message Queue](concepts/foundations/communication/message-queue/README.md)
    *   [PubSub](concepts/foundations/communication/pubsub/README.md)
    *   [Actor Model](concepts/foundations/communication/actor-model/README.md)
*   [Topology](concepts/foundations/topology/README.md)
    *   [Bus](concepts/foundations/topology/bus/README.md)
    *   [Mesh](concepts/foundations/topology/mesh/README.md)
    *   [Ring](concepts/foundations/topology/ring/README.md)
    *   [Star](concepts/foundations/topology/star/README.md)
    *   [Tree](concepts/foundations/topology/tree/README.md)

## Coordination & Consensus

*   [Coordination](concepts/foundations/coordination/README.md)
    *   [Distributed Locks](concepts/foundations/coordination/distributed-locks/README.md)
    *   [Leader Election](concepts/foundations/coordination/leader-election/README.md)
    *   [Quorum](concepts/foundations/coordination/quorum/README.md)
    *   [Event Streaming](concepts/foundations/coordination/event-streaming/README.md)
    *   [Gossip](concepts/foundations/coordination/gossip/README.md)
*   [Distributed Consensus](concepts/foundations/distributed-consensus/README.md)
    *   [Paxos](concepts/foundations/distributed-consensus/paxos/README.md)
    *   [Raft](concepts/foundations/distributed-consensus/raft/README.md)
*   [Concurrency Control](concepts/foundations/concurrency-control/README.md)
    *   [Optimistic Locking](concepts/foundations/concurrency-control/optimistic-locking/README.md)
    *   [Pessimistic Locking](concepts/foundations/concurrency-control/pessimistic-locking/README.md)
*   [Conflict Resolution](concepts/foundations/conflict-resolution/README.md)
    *   [Last Write Wins](concepts/foundations/conflict-resolution/last-write-wins/README.md)
    *   [Timestamps with Logical Clocks](concepts/foundations/conflict-resolution/timestamps-with-logical-clocks/README.md)
    *   [Vector Clocks](concepts/foundations/conflict-resolution/vector-clocks/README.md)
    *   [CRDTs](concepts/foundations/conflict-resolution/crdts/README.md)

## Reliability & Fault Tolerance

*   [Fault Tolerance](concepts/foundations/fault-tolerance/README.md)
    *   [Active-Active Cluster](concepts/foundations/fault-tolerance/active-active-cluster/README.md)
    *   [Active-Passive Failover](concepts/foundations/fault-tolerance/active-passive-failover/README.md)
    *   [Idempotency](concepts/foundations/fault-tolerance/idempotency/README.md)
    *   [Checkpoint](concepts/foundations/fault-tolerance/checkpoint/README.md)
    *   [Snapshot](concepts/foundations/fault-tolerance/snapshot/README.md)
    *   [Consensus Recovery](concepts/foundations/fault-tolerance/consensus-recovery/README.md)
    *   [Gossip Recovery](concepts/foundations/fault-tolerance/gossip-recovery/README.md)
    *   [Chaos Engineering](concepts/foundations/fault-tolerance/chaos-engineering/README.md)
*   [Reliability](concepts/foundations/reliability/README.md)

## Scalability & Performance

*   [Scalability](concepts/foundations/scalability/README.md)
*   [Scaling Patterns](concepts/patterns/scaling/README.md)
    *   [Horizontal Scaling](concepts/patterns/scaling/horizontal/README.md)
    *   [Vertical Scaling](concepts/patterns/scaling/vertical/README.md)
    *   [Distributed Caching](concepts/patterns/scaling/distributed-caching/README.md)
*   [Caching Infrastructure](concepts/infrastructure/caching/README.md)
*   [Load Balancing Infrastructure](concepts/infrastructure/load-balancing/README.md)

## Advanced Topics & Patterns

*   [System Modes](concepts/foundations/system-mode/README.md)
    *   [Event-Driven](concepts/foundations/system-mode/event-driven/README.md)
    *   [Eventually Consistent](concepts/foundations/system-mode/eventually-consistent/README.md)
    *   [Federated Multi-Cluster](concepts/foundations/system-mode/federated-multi-cluster/README.md)
    *   [Log-Based](concepts/foundations/system-mode/log-based/README.md)
    *   [Multi-Master](concepts/foundations/system-mode/multi-master/README.md)
    *   [Peer-to-Peer](concepts/foundations/system-mode/peer-to-peer/README.md)
    *   [Quorum-Based](concepts/foundations/system-mode/quorum-based/README.md)
    *   [Sharded Partitioned](concepts/foundations/system-mode/sharded-partitioned/README.md)
        *   [Directory-Based Sharding](concepts/foundations/system-mode/sharded-partitioned/directory-based-sharding/README.md)
        *   [Hash-Based Sharding](concepts/foundations/system-mode/sharded-partitioned/hash-based-sharding/README.md)
        *   [Range-Based Sharding](concepts/foundations/system-mode/sharded-partitioned/range-based-sharding/README.md)
    *   [Shared-Nothing](concepts/foundations/system-mode/shared-nothing/README.md)
    *   [CAP Tradeoff Tunable](concepts/foundations/system-mode/cap-tradeoff-tunable/README.md)
*   [Distributed Transactions](concepts/foundations/distributed-transactions/README.md)
    *   [Saga Pattern](concepts/foundations/distributed-transactions/saga-pattern/README.md)
    *   [Two-Phase Commit](concepts/foundations/distributed-transactions/two-phase-commit/README.md)
    *   [Three-Phase Commit](concepts/foundations/distributed-transactions/three-phase-commit/README.md)
*   [Data Replication Patterns](concepts/patterns/data-replication/README.md)
    *   [Async Replication](concepts/patterns/data-replication/async/README.md)
    *   [Semi-Sync Replication](concepts/patterns/data-replication/semi-sync/README.md)
    *   [Sync Replication](concepts/patterns/data-replication/sync/README.md)
    *   [Multi-Leader Replication](concepts/patterns/data-replication/multi-leader/README.md)
    *   [Multi-Source Replication](concepts/patterns/data-replication/multi-source/README.md)
    *   [CRDT Data Replication](concepts/patterns/data-replication/crdt/README.md)
*   [Messaging Patterns](concepts/patterns/messaging/README.md)
    *   [Message Queue Pattern](concepts/patterns/messaging/message-queue/README.md)
    *   [Publish-Subscribe Pattern](concepts/patterns/messaging/publish-subscribe/README.md)
*   [Observability Patterns](concepts/patterns/observability/README.md)
    *   [Distributed Tracing](concepts/patterns/observability/distributed-tracing/README.md)
*   [Circuit Breaker Pattern](concepts/patterns/circuit-breaker/README.md)
*   [Saga Pattern (Orchestration/Choreography)](concepts/patterns/saga/README.md)
*   [Service Discovery Patterns](concepts/patterns/service-discovery/README.md)
    *   [Client-Side Discovery](concepts/patterns/service-discovery/client-side-discovery/README.md)
    *   [Server-Side Discovery](concepts/patterns/service-discovery/server-side-discovery/README.md)
    *   [Centralized Discovery](concepts/patterns/service-discovery/centralized-discovery/README.md)
    *   [Decentralized Discovery](concepts/patterns/service-discovery/decentralized-discovery/README.md)
*   [API Gateways Infrastructure](concepts/infrastructure/api-gateways/README.md)
*   [Proxies Infrastructure](concepts/infrastructure/proxies/README.md)
*   [Service Mesh Infrastructure](concepts/infrastructure/service-mesh/README.md)
*   [Databases Infrastructure](concepts/infrastructure/databases/README.md)

## System Design

*   [Introduction to System Design](concepts/system-design/introduction.md)
*   [System Design Overview](concepts/system-design/README.md)

## Other Resources

*   [Security](concepts/foundations/security/README.md)
*   [Transparency](concepts/foundations/transparency/README.md)
*   [Glossary](GLOSSARY.md)
*   [Contributing](CONTRIBUTING.md)
