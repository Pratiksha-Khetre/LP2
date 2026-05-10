import heapq

def heuristic(board):
    h = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                h += 1
    return h


def a_star_4_queens():
    n = 4
    pq = []

    start = []
    heapq.heappush(pq, (0, start))

    while pq:
        f, board = heapq.heappop(pq)

        if len(board) == n:
            if heuristic(board) == 0:
                return board
            continue

        for row in range(n):
            new_board = board + [row]

            g = len(new_board)  
            h = heuristic(new_board)  
            f = g + h

            heapq.heappush(pq, (f, new_board))

    return None


solution = a_star_4_queens()

print("Solution:", solution)

print("\nBoard:")
for row in solution:
    for i in range(4):
        if i == row:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()