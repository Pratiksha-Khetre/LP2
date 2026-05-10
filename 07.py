def find(parent, x):
    if parent[x] == x:
        return x
    
    return find(parent, parent[x])

def kruskal(vertices, edges):

    parent = {}
    mst = []

    edges.sort(key = lambda x : x[2])

    total_cost = 0

    for v in vertices:
        parent[v] = v

    for u, v , weight in edges:

        root_u = find(parent, u)
        root_v = find(parent, v)

        if root_u != root_v:
            mst.append((u, v, weight))
            parent[root_u] = root_v
            total_cost += weight

    return total_cost, mst

vertices = ['A', 'B', 'C', 'D']

# Edges (u, v, weight)
edges = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 3)
]

cost, mst = kruskal(vertices, edges)

print("Total Cost : ", cost)

for i in mst:
    print(i)

import heapq

def prims(start, graph):

    visited = set()

    min_heap = [(0, start, -1)]

    total_cost = 0

    while min_heap:

        weight, node, parent = heapq.heappop(min_heap)

        if node not in visited:
            visited.add(node)
            total_cost += weight

            if parent != -1:
                print(parent , " ->  ", node," : ", weight )

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, neighbor, node))

    print("total cost : ", total_cost)

graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}

prims(0, graph)