import heapq

def dijkstra(start, graph):

    distance = {node : float ('inf') for node in graph}
    distance[start] = 0

    pq = [(0, start)]

    while pq:

        curr, node = heapq.heappop(pq)

        for neighbor, weight in graph[node]:
            new_weight = curr + weight

            if new_weight < distance[neighbor]:
                distance[neighbor] = new_weight

                heapq.heappush(pq, (new_weight, neighbor))
            
    return distance

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}


result = dijkstra('A', graph)
print(result)


def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

def kruskal(vertices , edges):

    edges.sort(key = lambda x : x[2])

    parent = {}
    mst = []

    total_cost = 0

    for v in vertices:
        parent[v] = v

    for u, v, weight in edges:

        root_u = find(parent, u)
        root_v = find(parent, v)

        if root_u != root_v:
            mst.append((u,v, weight))

            parent[root_u] = root_v

            total_cost += weight

    return mst, total_cost


vertices = ['A', 'B', 'C', 'D']

# Edges (u, v, weight)
edges = [
    ('A', 'B', 1),
    ('A', 'C', 4),
    ('B', 'C', 2),
    ('B', 'D', 5),
    ('C', 'D', 3)
]

mst , cost = kruskal(vertices, edges)

print("total cost : ", cost)

for i in mst:
    print(i)