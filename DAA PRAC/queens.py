# N-Queens Problem using Backtracking

n = int(input("Enter the value of n: "))

board = [[0 for _ in range(n)] for _ in range(n)]

# Place the first Queen
col = int(input("Enter column for first Queen (1 to n): "))
board[0][col - 1] = 1


# Check whether a Queen can be placed
def is_safe(row, col):

    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i = row - 1
    j = col - 1

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i = row - 1
    j = col + 1

    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


# Backtracking
def solve(row):

    if row == n:
        return True

    for col in range(n):

        if is_safe(row, col):
            board[row][col] = 1

            if solve(row + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False


# Solve remaining rows
if solve(1):
    print("\nFinal N-Queens Matrix:")

    for row in board:
        print(row)
else:
    print("No solution exists.")