import heapq

def job_schedule(jobs):

    jobs.sort(key = lambda x : x[2], reverse = True)
    max_deadline = max(job[1] for job in jobs)

    total_profit = 0

    slot = [-1] * max_deadline

    for job in jobs:

        job_id, deadline, profit = job

        for i in range(deadline-1, -1, -1):

            if slot[i] == -1:
                slot[i] = job_id
                total_profit += profit

                break

    print("Total Profit ", total_profit)
    print("Jobs ", [job for job in slot if job != -1])

jobs = [
    ('J1', 2, 100),
    ('J2', 1, 19),
    ('J3', 2, 27),
    ('J4', 1, 25),
    ('J5', 3, 15)
]

job_schedule(jobs)



def dijkstra(start, graph):

    distances = {node : float('inf') for node in graph}
    distances[start] = 0

    pq = [(0, start)]

    while pq :
        curr_dist, node = heapq.heappop(pq)


        for neighbor, weight in graph[node]:
            new_dist = curr_dist + weight

            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}


result = dijkstra('A', graph)
print(result)







