V, E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))

#print(edgeList)

from disjointsets3 import DisjointSets

s = DisjointSets(V)

for i in range(V):
    for j in edgeList:
        if j[0] == i:
            s.union(j[0], j[1])

v1, v2 = map(int, input().split())
#
miss = False
# for i in range(V-1):
#     if s.findset(i) != s.findset(i+1):
#         miss = True

if s.findset(v1) != s.findset(v2):
    miss = True

if miss:
    print("NO")
else:
    print("YES")
