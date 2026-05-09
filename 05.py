import heapq

# Selection SOrt

n = int(input("Enter size of array "))
arr = []

for i in range(n):
    num = int(input(f"Enter {i+1} element : "))
    arr.append(num)

for i in range(n):

    min_idx = i

    for j in range(i+1, n):
        if arr[j] < arr[min_idx]:
            min_idx = j

    arr[i] , arr[min_idx] = arr[min_idx], arr[i]

print("Sorted array is : ")
print(arr)

# MST using Prims_algo

def prims_mst(graph, start):
    visited = set()

    min_heap = [(0, start,-1)]

    total_sum = 0

    while min_heap:

        weight, node, parent = heapq.heappop(min_heap)

        if node not in visited:
            visited.add(node)
            total_sum += weight

            if parent != -1:
                print ( node , " -> " , parent , " " , weight )


            for neighbor, weight in graph[node]:

                if neighbor not in visited:
                    
                    heapq.heappush(min_heap, (weight, neighbor, node))
        
    print("total cost : ", total_sum)


graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)]
}

prims_mst(graph, 0)
