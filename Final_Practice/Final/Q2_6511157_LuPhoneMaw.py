#QUESTION 2 ACCOMPLISH!!!


V, E = map(int, input().split())
edgeList = []
for i in range(E):
    edgeList.append(tuple(map(int, input().split())))


class DisjointSets:
    def __init__(self, n): #n as input, which represents the number of elements in the disjoint set. 
        #Is self.p a list or a tuple? It is a list.
        self.p = list(range(n)) # p[i] is the parent pointer of item i in the disjoint set. list(range(n)) is a list of n items
        self.rank = [0]*n # rank[i] is the rank of item i. [0] is a list of 1 item 
                #[0] * n is a way to create a list of n items with each item is 0
        
     #determining the unique element that serves as the representative or root 
     # of a particular set or group of elements.   
    def findset(self, u): # find the representative of the set that contains u
        if self.p[u] == u: # if u is the representative of the set
            return u
        else:
            self.p[u] = self.findset(self.p[u])
            return self.p[u]

    def union(self, u,v):
        a = self.findset(u) # find the representative of the set that contains u
        b = self.findset(v) # find the representative of the set that contains v
        if self.rank[a] < self.rank[b]: # if rank of a is less than rank of b. 
                                        #This is checking the height of the tree
            self.p[a] = b       # make b as the parent of a
        else:
            self.p[b] = a  # make a as the parent of b
            if self.rank[a] == self.rank[b]: # if rank of a is equal to rank of b
                self.rank[a] += 1 # increase the rank of a by 1


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


# (base) richard@Lus-MacBook-Pro Final % python q2.py 
# 4 2
# 0 3
# 1 2
# 1 3
# NO
# (base) richard@Lus-MacBook-Pro Final % python q2.py
# 3 2
# 0 1
# 0 2
# 1 2
# YES
