#!/usr/bin/python3
"""
N Queens Problem Solver
"""
import sys

def is_valid(board, row, col):
    """
    Check if a queen can be placed on board at (row, col).
    """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N, row, board, solutions):
    """
    Use backtracking to find all solutions for N queens.
    """
    if row == N:
        solutions.append([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        if is_valid(board, row, col):
            board[row] = col
            solve_nqueens(N, row + 1, board, solutions)
            # No need to reset board[row] as it will be overwritten in the next iteration

def print_solutions(solutions):
    """
    Print all the solutions.
    """
    for solution in solutions:
        print(solution)

def main():
    """
    Main function to parse arguments and solve N Queens problem.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []
    board = [-1] * N
    solve_nqueens(N, 0, board, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    main()
