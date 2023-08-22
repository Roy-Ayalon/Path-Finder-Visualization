# Path-Finder-Visualization

This is my own project to show different path finding algorithms, with visualization.

# BFS

![bfs](https://github.com/Roy-Ayalon/Path-Finder-Visualization/assets/90352235/6922a590-86f3-4cf1-ad71-cbfe0e0366b7)




**Breadth-First Search Steps:**
1. Initialization: The algorithm starts by selecting a source node as the initial node. This node is added to the queue to mark it as visited.

2. Exploration: The algorithm explores the immediate neighbors (adjacent nodes) of the current node. These neighbors are added to the queue if they haven't been visited yet.

3. Queue Management: The algorithm uses a queue to manage the order in which nodes are visited. The first node added to the queue is the first to be visited, following a FIFO (First-In-First-Out) approach.

4. Level-wise Traversal: BFS visits nodes level by level. It starts with the source node, then moves to its neighbors, and subsequently to the neighbors' neighbors. This results in a breadth-first exploration.

5. Marking Visited Nodes: Visited nodes are marked to avoid revisiting them. This prevents infinite loops in cases of cyclic graphs.

6. Visualization: During each step, the visualization tool highlights the current node being visited and the nodes in the queue. This dynamic visualization helps you understand the order and progression of the algorithm.
