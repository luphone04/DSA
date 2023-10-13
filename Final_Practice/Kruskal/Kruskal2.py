def kruskal_mst(V, E, adj_list):
  """Finds the minimum spanning tree of a graph using Kruskal's algorithm.

  Args:
    V: The number of vertices in the graph.
    E: The number of edges in the graph.
    adj_list: A list of adjacency lists, where each adjacency list contains
      tuples of the form (neighbor, weight).

  Returns:
    A list of edges in the minimum spanning tree, sorted by weight.
  """



  #GIVES ERROR

  # Sort the edges by weight.
  edges = []
  for u in range(V):
    for v, w in adj_list[u]:
      edges.append((w, u, v))
  edges.sort()

  # Initialize the union-find data structure.
  uf = UnionFind(V)

  # Greedily add edges to the MST.
  mst = []
  for w, u, v in edges:
    if uf.find(u) != uf.find(v):
      mst.append((u, v, w))
      uf.union(u, v)

  return mst

class UnionFind:
  """A union-find data structure."""

  def __init__(self, n):
    self.parent = [i for i in range(n)]
    self.rank = [1 for i in range(n)]

  def find(self, x):
    if self.parent[x] != x:
      self.parent[x] = self.find(self.parent[x])
    return self.parent[x]

  def union(self, x, y):
    rx = self.find(x)
    ry = self.find(y)
    if rx == ry:
      return
    if self.rank[rx] < self.rank[ry]:
      self.parent[rx] = ry
    elif self.rank[rx] > self.rank[ry]:
      self.parent[ry] = rx
    else:
      self.parent[rx] = ry
      self.rank[ry] += 1


# Example usage:

V, E = map(int, input().split())
adj_list = [[] for v in range(V)]

for i in range(E):
  u, v, w = map(int, input().split())
  adj_list[u].append((v, w))
  adj_list[v].append((u, w))

mst = kruskal_mst(V, E, adj_list)

for u, v, w in mst:
  print(u, v, w)

