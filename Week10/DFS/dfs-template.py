graph_type = input()
if graph_type != "Directed Graph":
    print("DFS only works on Directed Graph")
    exit()

V,E = map(int, input().split())  # takes input for the number of vertices (V) and edges (E)
adj_list = [[] for v in range(V)] # initializes an adjacency list (adj_list) as an empty list of lists, 
                                  #where adj_list[i] will store the neighbors of vertex i
for i in range(E): 
    u,v = map(int, input().split())
    u -= 1 #convert them to 0-based indexing (assuming vertices are numbered from 1 to V in the input)
    v -= 1 #convert them to 0-based indexing (assuming vertices are numbered from 1 to V in the input)
    adj_list[u].append(v) # indicating that there is an edge from u to v.

color = ["WHITE"]*V  # (WHITE for unvisited, GREY for visited but not explored, BLACK for explored)
p = [None]*V #parent
time = 0
d = [-1]*V #discovery time
f = [-1]*V #finish time
# Write your Depth-First Search code below without function.
# Don't forget to make the initial dfs call! :)
time = 0

def dfs_visit(u):
    global time, d
    time += 1                   # increment time
    d[u] = time                #  assigns this value as the discovery time (d[u]) 
    color[u] = "GREY"               # mark u as visited , currently being explored

    for v in adj_list[u]: # iterates through all neighbors v of u
        if color[v] == "WHITE":     # if v is unvisited
            p[v] = u                # mark parent of the v as u
            dfs_visit(v)            # dfs-visit v, recursive

    color[u] = "BLACK"              # mark u as explored 
    time += 1                       # increment time
    f[u] = time                     # store the time at u's finish_time


for u in range(V):                  
    if color[u] == "WHITE":         # dfs-visit for every unvisited u
        dfs_visit(u)
# The code below is for printing output

for v in range(V):
    if d[v] == -1:
        dv = "undiscovered"
    else:
        dv = d[v]
    if f[v] == -1:
        fv = ""
    else:
        fv = f[v]
    if p[v] != None:
        pv = p[v]+1
    else:
        pv = "None"

    print("%d %5s" % (v+1, color[v]), dv, fv, pv)






