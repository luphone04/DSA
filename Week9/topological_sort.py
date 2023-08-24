
# A call to topological_sort must be with two arguments
# 1) The number of vertices of the Directed Acyclic Graph
# 2) The adjacency list of the graph

visited = []
stack = []

def DFS_visit(s, adj): 
    global visited, stack
    
    for v in adj[s]:
        if not visited[v]:
            visited[v] = True
            DFS_visit(v, adj)
    stack.append(s)

def topological_sort(V, adj):
    #V is the number of vertices of the graph and adj is the adjacency list of the graph
    global visited, stack
    
    visited = [False]*V
    for s in range(V):
        if not visited[s]:
            visited[s] = True
            DFS_visit(s, adj)
    stack.reverse()
    return stack


# Input: The first line contains two integers V and E, the number of vertices and edges of the graph.
# The next E lines contain two integers u and v, denoting that there is an edge from u to v.
# Output: A single line containing the vertices of the graph in topological order.
#Code
V, E = map(int, input().split()) #takes the number of vertices and edges as input
adj = [[] for _ in range(V)] #create "V" empty lists 
for _ in range(E): #takes the edges as input
    u, v = map(int, input().split())  #takes the vertices of the edge as input  
    adj[u].append(v) #adds the vertex v to the adjacency list of vertex u
print(*topological_sort(V, adj)) #calls the topological_sort function and prints the result
#The printed result is the topological order of the graph in the input  

# Sample Input:
# 6 6
# 5 2
# 5 0
# 4 0
# 4 1
# 2 3
# 3 1
