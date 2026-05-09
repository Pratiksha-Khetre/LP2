def dfs(node, graph, visited):
    if node not in visited:
        print(" ", node)
        visited.add(node)

        for neightbor in graph[node]:
            if neightbor not in visited:
                dfs(neightbor, graph, visited)

graph = {}

visited = set()

v = int(input("Enter number of vertex"))

for i in range(v):
    vertex = input(f"enter vertex name {i+1} ")
    graph[vertex] = []

e = int(input("Enter number of edges "))

for i in range(e):

    a = input("Enter first vertex of Edge ")
    b = input("Enter second vertex of Edge ")

    graph[a].append(b)
    graph[b].append(a)


start = input("enter starting node ")

print("DFS Traversal of Graph is ")
dfs(start, graph, visited)

