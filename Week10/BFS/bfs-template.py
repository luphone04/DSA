graph_type = input()
V,E = map(int, input().split()) # the number of vertices (nodes) and edges in the graph
adj_list = [[] for v in range(V)]
for i in range(E):
    u,v = map(int, input().split())
    u -= 1 #convert them to 0-based indexing (assuming vertices are numbered from 1 to V in the input)
    v -= 1 #convert them to 0-based indexing (assuming vertices are numbered from 1 to V in the input)
    adj_list[u].append(v) # indicating that there is an edge from u to v.
    if graph_type == "Undirected Graph":
        adj_list[v].append(u) # indicating that there is an edge from v to u.

color = ["WHITE"]*V # (WHITE for unvisited, GREY for visited but not explored, BLACK for explored)
d = [-1]*V  #store the distance from the source vertex to each vertex during BFS
p = [None]*V #store the parent vertex of each vertex during BFS

# Write your Breath-First Search code below without function.
# Don't forget to make the initial bfs call! :)
s = 0   #Source the start of BFS (inisialize as zero)
color[s] = "GREY"                       # mark source vertex of BFS as gery
d[s] = 0 #sets the distance of the source vertex s to 0 
p[s] = None # parent to None


Q = [s] # a queue Q to keep track of the vertices to be visited
while Q: #loop continues as long as the queue Q is not empty
    u = Q[0]  # u is the first element of Q (peek)
    del Q[0] # remove u from Q (dequeue)

    for v in adj_list[u]: #For each adjacent vertex v of u (found in the adjacency list of u),
        if color[v] == "WHITE":         # if v is unvisited
            color[v] = "GREY"           #If v is WHITE, it marks v as GREY
            d[v] = d[u] + 1             #sets its distance d[v] to the distance of u plus 1,
            p[v] = u                    #sets p[v] as u
            Q.append(v)                 #enqueues v into the queue Q

    color[u] = "BLACK"                  # mark u as explored

#code for printing
for v in range(V): #print the output for each vertex v in the order of their discovery
    if d[v] == -1: #if the vertex v is not reachable from the source vertex s (i.e., undiscovered),
        dv = "Inf" #it prints Inf for the distance d[v]
    else: #otherwise, it prints the distance d[v]
        dv = d[v] 
    if p[v] != None: #if the vertex v has a parent vertex p[v], it prints the parent vertex p[v]
        pv = p[v]+1 # (note that we add 1 to the index of the parent vertex p[v] to convert it to 1-based indexing)
    else: #otherwise, it prints None
        pv = "None"

    print("%d %5s" % (v+1, color[v]), dv, pv) 
    #"%d %5s" is a format string that prints the vertex number v+1 and the color of v



