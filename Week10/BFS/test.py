graph_type = input()
V, E = map(int, input().split())  # the number of vertices (nodes) and edges in the graph
adj_list = [[] for v in range(V)]

for i in range(E):  # CREATING EDGE edge(u,v) in the graph
    u, v = map(int, input().split())  # u represents the source vertex, and v represents the destination vertex
    u -= 1  # convert them to 0-based indexing (assuming vertices are numbered from 1 to V in the input)
    v -= 1  # convert them to 0-based indexing (assuming vertices are numbered from 1 to V in the input)
    adj_list[u].append(v)  # indicating that there is an edge from u to v.
    if graph_type == "Undirected Graph":
        adj_list[v].append(u)  # indicating that there is an edge from v to u.

# Print the adjacency list in the correct format
for u in range(V):
    print(f"{u + 1} -> {adj_list[u]}")
