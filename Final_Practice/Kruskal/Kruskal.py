#an implementation of Kruskal's algorithm to find the Minimum Spanning Tree (MST) in a graph
# find the MST of a graph and prints whether the graph is connected and the total weight of the MST if it exists

#PRINTED FROM THE "edgeList" VARIABLE
# [(0, 1, 2)]
# [(0, 1, 2), (0, 3, 4)]
# [(0, 1, 2), (0, 3, 4), (1, 2, 4)]
# [(0, 1, 2), (0, 3, 4), (1, 2, 4), (1, 3, 4)]
# [(0, 1, 2), (0, 3, 4), (1, 2, 4), (1, 3, 4), (1, 4, 3)]
# [(0, 1, 2), (0, 3, 4), (1, 2, 4), (1, 3, 4), (1, 4, 3), (1, 5, 1)]
# [(0, 1, 2), (0, 3, 4), (1, 2, 4), (1, 3, 4), (1, 4, 3), (1, 5, 1), (2, 5, 5)]
# [(0, 1, 2), (0, 3, 4), (1, 2, 4), (1, 3, 4), (1, 4, 3), (1, 5, 1), (2, 5, 5), (3, 4, 2)]
# [(0, 1, 2), (0, 3, 4), (1, 2, 4), (1, 3, 4), (1, 4, 3), (1, 5, 1), (2, 5, 5), (3, 4, 2), (4, 5, 5)]

# 0
# 1
# 2
# 3
# 4
# 3 3
# 3 3

#SORTED EDGELIST
# [(1, 5, 1), (0, 1, 2), (3, 4, 2), (1, 4, 3), (0, 3, 4), (1, 2, 4), (1, 3, 4), (2, 5, 5), (4, 5, 5)]

#the MST GRAPH
# 1 5 1
# 0 1 2
# 3 4 2
# 1 4 3
# 0 3 4
# 1 2 4
# 1 3 4
# 2 5 5
# 4 5 5

#CHECK CONNECTED
# Connected

#TOTAL MST WEIGHT
# 12


V,E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))
    print(edgeList)

from disjointsets3 import DisjointSets

s = DisjointSets(V)

#Merge both

edgeList.sort(key = lambda a:a[2])
print(edgeList)


W = 0
edgeCount = 0
for u,v,w in edgeList:
    print(u,v,w)
    if s.findset(u) != s.findset(v): # check whether they belong to different groups
        # add weight w to total weight W
        W += w 
        # union u and v
        s.union(u,v) 
        # add 1 to edgecount since we union-ed u and v
        edgeCount += 1

if edgeCount >= V - 1: # a graph is connected when |E| = |V| - 1
    print("Connected")
    print(W) # print out total weight

else:
    print("Not Connected")