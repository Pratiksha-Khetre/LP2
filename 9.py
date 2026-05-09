def print_solutions(solutions, n):
    print(f"\nTotal Solutions: {len(solutions)}")
    for sol in solutions:
        for i in range(n):
            row = ['.'] * n
            row[sol[i]] = 'Q'
            print(" ".join(row))
        print()


# ------------------ BACKTRACKING ------------------
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_backtracking(n):
    def solve(row):
        if row == n:
            solutions.append(board[:])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve(row + 1)

    board = [-1] * n
    solutions = []
    solve(0)
    return solutions


# ------------------ BRANCH & BOUND ------------------
def solve_branch_and_bound(n):
    def solve(row):
        if row == n:
            solutions.append(board[:])
            return
        
        for col in range(n):
            if not cols[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
                board[row] = col
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = True
                
                solve(row + 1)
                
                cols[col] = diag1[row + col] = diag2[row - col + n - 1] = False

    board = [-1] * n
    cols = [False] * n
    diag1 = [False] * (2 * n)
    diag2 = [False] * (2 * n)
    solutions = []
    
    solve(0)
    return solutions


# ------------------ MAIN ------------------
n = int(input("Enter number of queens: "))

print("\n=== Backtracking Solution ===")
bt_solutions = solve_backtracking(n)
print_solutions(bt_solutions, n)

print("\n=== Branch and Bound Solution ===")
bb_solutions = solve_branch_and_bound(n)
print_solutions(bb_solutions, n)