from collections import deque # double-ended queue

# Write a program which reads an directed graph $G = (V, E)$, and finds the shortest distance from
# vertex $1$ to each vertex (the number of edges in the shortest path). Vertices are identified by 
# IDs $1, 2, ... n$.

#TAKE IN THE NUMBER OF VERTICES AS A FIRST INPUT

#THEN TAKE IN THE ADJACENCY LIST AS THE NEXT INPUTS

#THEN THE OUTPUT IS the ID of the vertex and its distance from the source vertex(1)

#IF no path exists, print -1

#Example INPUT 
# 4
# 1 2 2 4
# 2 1 4
# 3 0
# 4 1 3

#OUTPUT
# 1 0
# 2 1
# 3 2
# 4 1

def bfs(graph, n):
    # Initialize distances and visited array
    distances = [-1] * (n + 1)
    visited = [False] * (n + 1)

    # Start BFS from vertex 1
    distances[1] = 0
    visited[1] = True
    queue = deque([1])

    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                distances[v] = distances[u] + 1
                queue.append(v)

    return distances

# Read input
n = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    data = list(map(int, input().split()))
    u, k, *adj_list = data
    graph[u] = adj_list

# Find shortest distances
distances = bfs(graph, n)

# Print the results
for u in range(1, n + 1):
    print(u, distances[u])