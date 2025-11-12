def print_board(board):
    for r in range(len(board)):
        print(' '.join('Q' if board[r] == c else '.' for c in range(len(board))))
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i] in {col, col - row + i, col + row - i}:
            return False
    return True

def backtrack(board, row, n):
    if row == n:
        print_board(board)
        return True
    found = False
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            found |= backtrack(board, row + 1, n)
    return found

def branch_bound(row, cols, d1, d2, board, n):
    if row == n:
        print_board(board)
        return True
    found = False
    for col in range(n):
        if col not in cols and row - col not in d1 and row + col not in d2:
            board[row] = col
            found |= branch_bound(row + 1, cols | {col}, d1 | {row - col}, d2 | {row + col}, board, n)
    return found

if __name__ == "__main__":
    n = 4
    print("=== N-Queens (Backtracking) ===")
    if not backtrack([-1]*n, 0, n):
        print("No solution!\n")

    print("=== N-Queens (Branch & Bound) ===")
    if not branch_bound(0, set(), set(), set(), [-1]*n, n):
        print("No solution!\n")
