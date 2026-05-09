from collections import deque

def bfs(node, graph):

    visited = set()

    queue = deque()
    visited = set()

    queue.append(node)
    visited.add(node)
    
    while queue:
        a = queue.popleft()
        print(" ", a)

        for neighbor in graph[a]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

graph = {}

v = int(input("Enter Number of Vertex : "))

for i in range(v):
    vertex = input(f"Enter vertex {i+1} : ")
    graph[vertex] = []

u = int(input("Enter Number of Edges : "))

for i in range(u):
    a = input("Enter first edge : ")
    b = input("Enter second edge : ")

    graph[a].append(b)
    graph[b].append(a)

start = input("Enter Starting Node : ")

print("BFS Traversal : ")
bfs(start, graph)
    