from topological_sort import *
#DIRECTED GRAPH
#used to linearly order the vertices of a directed acyclic graph (DAG) in such a way that 
# for every directed edge (u, v), vertex u comes before vertex v in the ordering. I


# EdgeList: [[0, 1], [1, 2], [3, 2], [3, 4], [4, 5], [2, 5], [0, 7], [6, 7]]
# VertexList: [0, 1, 1, 2, 3, 2, 3, 4, 4, 5, 2, 5, 0, 7, 6, 7]
# Sorted vertex list: [0, 1, 2, 3, 4, 5, 6, 7]

n, e = map(int, input().split()) # n is number of vertices, e is number of edge
EdgeList = []

for i in range(e):
    x = list(map(int, input().split()))
    EdgeList.append(x)

print(f"EdgeList: {EdgeList}")

vertexList = []
for i in range(len(EdgeList)):
    for j in range(2):
        vertexList.append(EdgeList[i][j])
print(f"VertexList: {vertexList}")

vertexList = list(set(vertexList)) #remove duplicate
vertexList.sort()
print(f"Sorted vertex list: {vertexList}")

vertices = len(vertexList)

# The code iterates through each vertex in the sorted vertex list and, for each vertex,
#  checks the edges to find its adjacent vertices.

#For example, for vertex 0, the code finds that it's adjacent to vertex 1 and 7.

ADJList = []
for i in range(len(vertexList)):
    temp = [vertexList[i]]
    for edge in EdgeList:
        if edge[0] == vertexList[i]:
            temp.append(edge[1])

    ADJList.append(temp)

# Print the adjacency list only once
print("Adjacency List:")
for item in ADJList:
    print(item)

result = topological_sort(len(vertexList),ADJList)

print("===================")

#The result of the topological sort is printed:
# ensures that each vertex comes after its dependencies in the directed acyclic graph. 
# For example, vertex 2 depends on vertex 1, so vertex 1 comes before vertex 2 in the topological order
#[6, 3, 4, 0, 7, 1, 2, 5]
print(result)