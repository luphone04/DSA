
import heapq

def shortest_path(graph, start, end):
    # Initialize distances to all vertices as infinity except the start vertex
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    # Priority queue to keep track of vertices to visit next
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Skip if we have already found a shorter path to this vertex
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # If this path is shorter than the previously recorded distance, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances[end]

# Parse input
n, m = map(int, input().split())
graph = {i: {} for i in range(1, n + 1)}

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u][v] = w

# Find the shortest path from 1 to N
shortest_distance = shortest_path(graph, 1, n)

# Print the result
print(shortest_distance)
