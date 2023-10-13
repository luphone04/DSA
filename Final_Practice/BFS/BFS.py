from collections import defaultdict, deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            queue.extend(neighbour for neighbour in graph[node] if neighbour not in visited)

    return traversal_order

def main():
    edge_list = """2-8
    2-1
    2-3
    2-6
    6-3
    4-3
    7-3
    6-4
    6-5
    8-2
    1-2
    3-2
    6-2
    3-6
    3-7
    3-4
    4-6
    5-6"""

    start_node = "1"

    edges = edge_list.split('\n')
    graph = defaultdict(list)

    for edge in edges:
        src, dest = map(str.strip, edge.split('-'))
        graph[src].append(dest)
        graph[dest].append(src)

    traversal_order = bfs(graph, start_node)

    print("BFS Traversal Order:")
    print(" -> ".join(traversal_order))

if __name__ == "__main__":
    main()
