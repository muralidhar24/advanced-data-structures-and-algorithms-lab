def solve_n_queens(n):
    """
    Solves the N-Queens problem using backtracking.

    Parameters:
        n: Number of queens and size of the chessboard (n x n).

    Returns:
        List of solutions, where each solution is represented as a list of column indices.
    """
    solutions = []

    def is_safe(board, row, col):
        # Check the column and diagonals
        for i in range(row):
            if board[i] == col or \
               board[i] - i == col - row or \
               board[i] + i == col + row:
                return False
        return True

    def backtrack(board, row):
        # Base case: If all queens are placed, add the solution
        if row == n:
            solutions.append(board[:])
            return

        # Try placing a queen in each column
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col  # Place the queen
                backtrack(board, row + 1)  # Recur for the next row
                board[row] = -1  # Backtrack (remove the queen)

    # Initialize the board with -1 (indicating no queen is placed)
    board = [-1] * n
    backtrack(board, 0)
    return solutions


def print_solutions(solutions, n):
    """
    Prints the solutions in a chessboard format.
    """
    for solution in solutions:
        for row in solution:
            print("".join("Q" if col == row else "." for col in range(n)))
        print("\n")


# Example usage
n = 8  # Change this to solve for a different size
solutions = solve_n_queens(n)
print_solutions(solutions, n)
print(f"Total solutions for {n}-Queens: {len(solutions)}")


