#COULDN"T RUN THE GIVEN TASK BUT
#ABLE TO WRITE CODE FOR adj_list and matrix, given the graph(edge_list)

def edge_list_to_adjacency_list(edge_list, directed=False):
    adjacency_list = {}

    def add_edge(adj_list, node1, node2):
        if node1 not in adj_list:
            adj_list[node1] = []
        adj_list[node1].append(node2)

    for edge in edge_list:
        if len(edge) == 2:
            node1, node2 = edge
            add_edge(adjacency_list, node1, node2)
            if not directed:
                add_edge(adjacency_list, node2, node1)
        else:
            print(f"Invalid edge: {edge}")

    return adjacency_list

def adjacency_list_to_matrix(adjacency_list, nodes):
    matrix = [[0] * len(nodes) for _ in range(len(nodes))]

    node_index = {node: index for index, node in enumerate(sorted(nodes))}

    for node, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            matrix[node_index[node]][node_index[neighbor]] = 1
            matrix[node_index[neighbor]][node_index[node]] = 1

    return matrix

# Input edge list as a list of tuples or lists
edge_list = [("a", "b"), ("b", "c"), ("c", "a"), ("b", "d"), ("d", "a"), ("d", "e"), ("e", "b")]

# Get a list of all nodes
nodes = list(set(node for edge in edge_list for node in edge))

# Convert to adjacency list for an undirected graph
adjacency_list_undirected = edge_list_to_adjacency_list(edge_list)
print("Undirected Graph Adjacency List:")
for node, neighbors in adjacency_list_undirected.items():
    print(f"{node} -> {', '.join(neighbors)}")
    
# Convert adjacency list to adjacency matrix
adjacency_matrix = adjacency_list_to_matrix(adjacency_list_undirected, nodes)
print("\nUndirected Graph Adjacency Matrix:")
for row in adjacency_matrix:
    print(" ".join(map(str, row)))

