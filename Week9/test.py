# Import the topological_sort module
from topological_sort import *

V, E = map(int, input().split()) 
adj = [[] for _ in range(V)] 
for _ in range(E): 
    u, v = map(int, input().split())  
    adj[u].append(v) 
print(*topological_sort(V, adj))