V,E = map(int, input().split()) # V: number of vertices, E: number of edges
edgeList = [] # list of edges
for i in range(E): # read all edges
    edgeList.append(tuple(map(int, input().split()))) 
    # append an edge to the list of edges and convert the edge to a tuple of 3 elements (u,v,w) 
    # where u and v are vertices and w is the weight of the edge 

from disjointsets3 import DisjointSets

s = DisjointSets(V)

# Write the code below
edgeList.sort(key = lambda x: x[2]) 
for u,v,w in edgeList:
    if s.findset(u) != s.findset(v):
        print(u,v,w)
        s.union(u,v)

print(s.p)



    
