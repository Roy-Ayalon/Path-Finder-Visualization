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

7. # DFS

8. ![dfs](https://github.com/Roy-Ayalon/Path-Finder-Visualization/assets/90352235/37d03a4a-a720-49fd-8502-66286c8cdb7c)



**Depth-First Search Steps:**

1. Choose a Starting Node: Select a node from the graph/tree to begin the traversal. This node is often referred to as the "root" for trees or "start" for graphs.

2. Visit the Starting Node: Mark the chosen starting node as visited or processed. This step may involve performing an operation on the node, depending on the problem you're trying to solve.

3. Explore Adjacent/Connected Nodes: Visit any unvisited nodes adjacent to the current node. You can choose any unvisited adjacent node, or you may follow a specific order, like left to right, top to bottom, etc., depending on your requirements.

4. Recursively Apply DFS: Repeat steps 2 and 3 for the chosen adjacent node. This step involves recursively applying the DFS algorithm to the adjacent node. In other words, you perform steps 2 and 3 on the adjacent node, treating it as your new current node.

5. Backtrack: If there are no more unvisited nodes adjacent to the current node, backtrack to the previous node and continue exploring unvisited nodes from there.

6. Repeat: Continue steps 2-5 until all nodes have been visited or until you've reached your desired goal (e.g., finding a specific node in the graph).

7. Termination: The algorithm terminates when you have visited all nodes, or you have achieved your specific objective, such as finding a target node.

