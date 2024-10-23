# Function to print the Sudoku grid
def print_board(board):
    for row in board:
        print(" ".join(str(cell) for cell in row))

# Function to check if placing num at board[row][col] is valid
def is_valid(board, row, col, num):
    # Check if num is in the current row
    if num in board[row]:
        return False

    # Check if num is in the current column
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check if num is in the current 3x3 sub-grid
    sub_grid_row_start = (row // 3) * 3
    sub_grid_col_start = (col // 3) * 3
    for i in range(sub_grid_row_start, sub_grid_row_start + 3):
        for j in range(sub_grid_col_start, sub_grid_col_start + 3):
            if board[i][j] == num:
                return False

    return True

# Function to find the next empty cell
def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None

# Backtracking Sudoku solver function
def solve_sudoku(board):
    # Find the next empty cell
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True  # No empty cells, solution found
    row, col = empty_cell

    # Try placing numbers 1-9 in the empty cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num  # Place the number

            # Recursively try to solve the rest of the board
            if solve_sudoku(board):
                return True

            # If placing num doesn't lead to a solution, backtrack
            board[row][col] = 0

    return False  # No valid number leads to a solution

# Example Sudoku puzzle (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Solve the Sudoku puzzle
if solve_sudoku(sudoku_board):
    print("Sudoku solved successfully:")
    print_board(sudoku_board)
else:
    print("No solution exists for the given Sudoku puzzle.")
