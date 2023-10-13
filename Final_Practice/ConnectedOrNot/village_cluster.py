class DisjointSets:
    def __init__(self, n):
        self.p = list(range(n))
        self.rank = [0] * n

    def findset(self, u):
        if self.p[u] == u: 
            return u
        else:
            self.p[u] = self.findset(self.p[u])
            return self.p[u]

    def union(self, u, v):
        a = self.findset(u)
        b = self.findset(v)
        if self.rank[a] < self.rank[b]:
            self.p[a] = b
        else:
            self.p[b] = a
            if self.rank[a] == self.rank[b]:
                self.rank[a] += 1

def kruskal(graph, k):
    graph.sort(key=lambda edge: edge[2])  # Sort edges by weight
    V = len(graph)
    s = DisjointSets(V)
    clusters = V  # Initially, each vertex is in its own cluster
    smallest_gap = float('inf')

    for u, v, w in graph:
        if s.findset(u) != s.findset(v):
            if clusters == k:  # Stop when we have k clusters
                smallest_gap = w  # Update the smallest gap weight
                break
            s.union(u, v)
            clusters -= 1

    return smallest_gap

if __name__ == '__main__':
    # Read the edge list and k as input
    V, E = map(int, input().split())
    edgeList = []
    for i in range(E):
        edgeList.append(tuple(map(int, input().split())))
    k = int(input())

    # Calculate the smallest gap weight of the maximally separated k-clustering
    smallest_gap = kruskal(edgeList, k)

    # Output the smallest gap weight
    print(smallest_gap)
