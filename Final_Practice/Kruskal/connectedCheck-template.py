#implementation of Kruskal's algorithm for finding the minimum spanning tree (MST) of a graph


#EXAMPLE OUTPUT( 1.in as example input file)
#The list of edges
#[(0, 1, 2), (0, 3, 4), (1, 2, 4), (1, 3, 4), (1, 4, 3), (1, 5, 1), (2, 5, 5), (3, 4, 2), (4, 5, 5)]

#These are list of vertices
# 0
# 1
# 2
# 3
# 4

#result of the s.findset(3) operation. 
#It suggests that vertex 3 belongs to a set with the representative 3.
# 3 3
# 3 3

# Connected

# Minimum Spanning Tree (MST) found by Kruskal's algorithm. 
# 12

# Graph Connected

#construct the Minimum Spanning Tree (MST) and displays the MST edges, represented as pairs of vertices.
# [(1, 5), (0, 1), (3, 4), (1, 4), (1, 2)]

# 12


V,E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

print(edgeList)


from disjointsets3 import DisjointSets

s = DisjointSets(V)

# Complete the code below

edgeList.sort(key = lambda a:a[2])
W = 0
edgeCount = 0


for u,v,w in edgeList:
    if s.findset(u) != s.findset(v):
        W += w
        s.union(u,v)
        edgeCount += 1

if edgeCount == V - 1:
    #print("HERE",edgeCount, V-1)
    print("Connected")
    print(W)

else:
    print("Not Connected")


for u,v,_ in edgeList:
    s.union(u,v)

connected = True
prev = s.findset(v)
for v in range(V):
    if s.findset(v) != prev:
        print("Graph not connected")
        connected = False
        break
else:
    print("Graph Connected")



if connected:
    s = DisjointSets(V)
    A = []
    W = 0

    edgeList.sort(key = lambda a:a[2])
    for u,v,w in edgeList:
        if s.findset(u) != s.findset(v):
            W += w
            A.append((u,v))
            s.union(u,v)

    print(A)
    print(W)




#Merge both


    
