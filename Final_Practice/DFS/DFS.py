from collections import defaultdict


#INPUT IS LIST OF EDGES

#OUTPUT IS LIST OF VERTICES WITH DISCOVERY AND FINISH TIMES

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.time = 1

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, discovery, finish):
        discovery[v] = self.time
        self.time += 1

        for neighbor in self.graph[v]:
            if discovery[neighbor] == -1:
                self.dfs(neighbor, discovery, finish)

        finish[v] = self.time
        self.time += 1

    def dfs_main(self):
        vertices = list(self.graph.keys())
        num_vertices = len(vertices)
        discovery = {vertex: -1 for vertex in vertices}
        finish = {vertex: -1 for vertex in vertices}

        for vertex in vertices:
            if discovery[vertex] == -1:
                self.dfs(vertex, discovery, finish)

        for vertex in vertices:
            print(f"{vertex} {discovery[vertex]} {finish[vertex]}")

# Input edge list
edge_list = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('D', 'F'),
    ('F', 'E'),
    ('E', 'D')
]

g = Graph()

for edge in edge_list:
    g.add_edge(edge[0], edge[1])

g.dfs_main()
