from collections import defaultdict
import heapq

def shortest_path(graph, start, end):
    """
    Find the shortest path between start and end nodes in a weighted graph
    using Dijkstra's algorithm.
    
    Args:
        graph: Dictionary mapping nodes to a list of (neighbor, distance) tuples
        start: Starting node
        end: Target node
        
    Returns:
        Distance of the shortest path and the path as a list of nodes
    """
    # Priority queue for distances
    distances = [(0, start, [])]  # (distance, node, path)
    # Dictionary to keep track of visited nodes
    visited = defaultdict(lambda: float('infinity'))
    visited[start] = 0
    
    while distances:
        current_distance, current_node, path = heapq.heappop(distances)
        
        # If we've reached our destination
        if current_node == end:
            return current_distance, path + [current_node]
        
        # If we've found a longer path to current_node, skip
        if current_distance > visited[current_node]:
            continue
            
        # Check all neighbors
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If we've found a shorter path to the neighbor
            if distance < visited[neighbor]:
                visited[neighbor] = distance
                heapq.heappush(distances, (distance, neighbor, path + [current_node]))
    
    return float('infinity'), None  # No path found

# Example graph representation
sample_graph = {
    'A': [('B', 5), ('C', 3)],
    'B': [('A', 5), ('C', 1), ('D', 2)],
    'C': [('A', 3), ('B', 1), ('D', 6)],
    'D': [('B', 2), ('C', 6), ('E', 4)],
    'E': [('D', 4)]
}

# Find the shortest path from 'A' to 'E'
distance, path = shortest_path(sample_graph, 'A', 'E')
print(f"Shortest distance: {distance}")
print(f"Shortest path: {' -> '.join(path)}")