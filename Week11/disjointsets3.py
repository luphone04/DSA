
class DisjointSets:
    def __init__(self, n):
        #Is self.p a list or a tuple? It is a list.
        self.p = list(range(n)) # p[i] is the parent pointer of item i in the disjoint set. list(range(n)) is a list of n items
        self.rank = [0]*n # rank[i] is the rank of item i. [0] is a list of 1 item 
                #[0] * n is a way to create a list of n items with each item is 0
        
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





# example

djs = DisjointSets(5) # create a disjoint set with 5 items
for i in range(5): 
    print(djs.findset(i)) # print the representative of the set that contains i

djs.union(3,4)
print(djs.findset(3), djs.findset(4))

djs.union(4,1)
print(djs.findset(4), djs.findset(1))


