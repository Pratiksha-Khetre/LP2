import heapq

def heuristic(start, goal):
    count = 0

    for i in range(3):
        for j in range(3):
            if start[i][j] != goal[i][j] and start[i][j] != 0:
                count = count + 1
    
    return count

def A_star(start, goal):

    # f,g,state
    pq = []
    heapq.heappush(pq, (0, 0 , start))

    visited = []

    while pq:
        f, g, state = heapq.heappop(pq)

        if state == goal:
            return state
        
        visited.append(state)

        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    x, y = i, j

                moves = [(0,1), (0,-1), (1,0), (-1,0)]

        for dx, dy in moves:
            nx, ny = dx+x, dy+y

            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in state]

                new_state[x][y], new_state[nx][ny] = \
                new_state[nx][ny], new_state[x][y]

                if new_state not in visited:
                    h = heuristic(new_state, goal)

                    heapq.heappush(
                        pq, 
                        (g+h+1, g+1, new_state)
                    )

    return None

start = [[1,2,3],
         [4,0,6],
         [7,5,8]]

goal = [[1,2,3],
        [4,5,6],
        [7,8,0]]

result = A_star(start, goal)

for i in result:
    print(i)