# Define the graph as an adjacency list
graph = {
    'A': ['B', 'D'],
    'B': ['C'],
    'C': ['D'],
    'D': ['A']
}  

# Initialize visited dictionary
visited = {node: False for node in graph}

# Recursive DFS function
def DFS_VISIT(node):
    # Mark the current node as visited
    visited[node] = True            
    # Process the current node
    print(node, end=" ")            
    
    # Explore all neighbors
    for neighbor in graph[node]:
        if not visited[neighbor]:   
            # If the neighbor is unvisited
            DFS_VISIT(neighbor)

# Main DFS function
def DEF(graph):
    # Initialize all vertices as unvisited
    for node in graph:
        visited[node] = False

    # Start DFS for each unvisited vertex
    for node in graph:
        if not visited[node]:
            DFS_VISIT(node)

print("DFS Traversal:")
DEF(graph)
