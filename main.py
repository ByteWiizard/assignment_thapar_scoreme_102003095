
### 2. `main.py`


"""
Assignment: Implement the most efficient algorithm to solve the given problem.

Problem Statement:
You are given a Directed Acyclic Graph (DAG) with `n` nodes, numbered from `0` to `n-1`.
The graph is represented as an adjacency list where `graph[i]` is a list of tuples `(j, w)`,
representing an edge from node `i` to node `j` with weight `w`. Your task is to find the longest
path in the graph starting from any node.

Function Signature:
def longest_path(graph: list) -> int:

Parameters:
- graph (list): A list of lists, where `graph[i]` contains tuples `(j, w)` representing an edge
  from node `i` to node `j` with weight `w`.

Returns:
- int: The length of the longest path in the graph.

Example:
>>> graph = [
...     [(1, 3), (2, 2)],
...     [(3, 4)],
...     [(3, 1)],
...     []
... ]
>>> longest_path(graph)
7
"""

def longest_path(graph: list) -> int:
    # Your implementation goes here
    topological_order = topological_sort(graph)
    return calculate_longest_path(graph,topological_order)
    

# Helper function to perform topological sort
def topological_sort(graph):
    # Your implementation goes here

    def dfs(node,visited,stack):
        visited[node] = True
        for neighbor, weight in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited, stack)
        stack.append(node)

    visited = [False] * len(graph)
    stack = []
    for i in range(len(graph)):
        if not visited[i]:
            dfs(i, visited, stack)
    
    stack.reverse()
    return stack
  

# Function to calculate longest path using topological sort
def calculate_longest_path(graph, topo_order):
    # Your implementation goes here

    dist = [-float('inf')] * len(graph)
    dist[0] = 0


    for node in topo_order:
        if dist[node] != -float('inf'):
            for neighbor, weight in graph[node]:
                if dist[neighbor] < dist[node] + weight:
                    dist[neighbor] = dist[node] + weight
    
    return max(dist)
    
