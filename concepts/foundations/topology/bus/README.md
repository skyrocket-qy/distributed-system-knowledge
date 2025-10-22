# Bus Topology

This section explains the Bus topology in distributed systems.

## Which service use it?



-   **Early Ethernet Networks:** Historically, 10Base2 (ThinNet) and 10Base5 (ThickNet) Ethernet networks used a bus topology where all devices were connected to a single coaxial cable.

-   **Industrial Control Systems (e.g., CAN bus):** In automotive and industrial automation, bus topologies like CAN (Controller Area Network) are used for communication between various electronic control units (ECUs) and sensors.

-   **Embedded Systems:** Simple embedded systems or sensor networks might use a bus topology for inter-component communication due to its simplicity and low cost.

-   **Peripheral Connections:** Internally, a computer's PCI bus or USB bus can be seen as a form of bus topology, where multiple devices share a common communication path.

## Related Concepts

-   **Topology:** Bus topology is a simple network arrangement where all nodes are connected to a single, shared communication line, making it easy to implement but with inherent limitations. [Explore other Network Topologies](../README.md).

-   **Star Topology:** In contrast to a bus, a star topology connects all nodes to a central hub, which simplifies fault isolation but introduces the hub as a potential single point of failure. [Compare with Star Topology](../star/README.md).

-   **Tree Topology:** Bus topology can sometimes form the backbone of a tree topology, where multiple star networks or segments are connected to a central bus line, creating a hierarchical structure. [Compare with Tree Topology](../tree/README.md).

-   **Communication:** In a bus topology, all communication travels along the single shared medium, meaning all nodes receive all transmissions, which can lead to collisions and reduced efficiency with increased traffic. [Explore Communication Patterns](../../communication/README.md).

-   **Fault Tolerance:** A significant drawback of the bus topology is its single point of failure; a break in the main bus cable or a failure of a single node can disrupt communication for the entire network. [Understand Fault Tolerance](../../fault-tolerance/README.md).
