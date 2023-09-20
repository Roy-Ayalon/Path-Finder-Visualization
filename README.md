# Path-Finder-Visualization

This is my own project to show different path finding algorithms, with visualization.

# BFS

![bfs final](https://github.com/Roy-Ayalon/Path-Finder-Visualization/assets/90352235/bd8f15f0-0533-4c6d-ac3f-64e5204fdd9f)



**Breadth-First Search Steps:**
1. Initialization: The algorithm starts by selecting a source node as the initial node. This node is added to the queue to mark it as visited.

2. Exploration: The algorithm explores the immediate neighbors (adjacent nodes) of the current node. These neighbors are added to the queue if they haven't been visited yet.

3. Queue Management: The algorithm uses a queue to manage the order in which nodes are visited. The first node added to the queue is the first to be visited, following a FIFO (First-In-First-Out) approach.

4. Level-wise Traversal: BFS visits nodes level by level. It starts with the source node, then moves to its neighbors, and subsequently to the neighbors' neighbors. This results in a breadth-first exploration.

5. Marking Visited Nodes: Visited nodes are marked to avoid revisiting them. This prevents infinite loops in cases of cyclic graphs.

6. Visualization: During each step, the visualization tool highlights the current node being visited and the nodes in the queue. This dynamic visualization helps you understand the order and progression of the algorithm.

 # DFS

![dfs final](https://github.com/Roy-Ayalon/Path-Finder-Visualization/assets/90352235/8e883c48-7845-4b25-8a60-958d86d5e4e5)



**Depth-First Search Steps:**

1. Choose a Starting Node: Select a node from the graph/tree to begin the traversal. This node is often referred to as the "root" for trees or "start" for graphs.

2. Visit the Starting Node: Mark the chosen starting node as visited or processed. This step may involve performing an operation on the node, depending on the problem you're trying to solve.

3. Explore Adjacent/Connected Nodes: Visit any unvisited nodes adjacent to the current node. You can choose any unvisited adjacent node, or you may follow a specific order, like left to right, top to bottom, etc., depending on your requirements.

4. Recursively Apply DFS: Repeat steps 2 and 3 for the chosen adjacent node. This step involves recursively applying the DFS algorithm to the adjacent node. In other words, you perform steps 2 and 3 on the adjacent node, treating it as your new current node.

5. Backtrack: If there are no more unvisited nodes adjacent to the current node, backtrack to the previous node and continue exploring unvisited nodes from there.

6. Repeat: Continue steps 2-5 until all nodes have been visited or until you've reached your desired goal (e.g., finding a specific node in the graph).

7. Termination: The algorithm terminates when you have visited all nodes, or you have achieved your specific objective, such as finding a target node.


# Dijkstra

![dijkstra gif](https://github.com/Roy-Ayalon/Path-Finder-Visualization/assets/90352235/079d90a4-9b34-4f62-9be2-7c0294312f16)

**Dijkstra Steps:**

1. Select the Next Vertex: Find the vertex with the smallest distance value among the unvisited vertices. Initially, this will be the source vertex.

2. Relaxation: For the selected vertex, consider all its unvisited neighbors. Calculate their tentative distance through the current vertex. Compare this newly calculated tentative distance to the current assigned value and update it if the new distance is smaller. Essentially, you are improving the known distances to each neighboring vertex through the current vertex.

3. Mark as Visited: Once you've considered all the neighbors of the current vertex, mark it as visited (or add it to the visited set) to prevent revisiting it.

4. Repeat: Repeat steps 2 through 4 until you have visited all vertices or until the vertex with the smallest distance among unvisited vertices is at infinity (indicating that there is no path to it).


