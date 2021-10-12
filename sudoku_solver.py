rows = 9
cols = 9


def solve(board):
    if not isinstance(board, list):
        raise TypeError(f'Not a board: {board}')
    if not board:
        raise ValueError(f'Empty board: {board}')

    rows = len(board)
    cols = len(board[0])

    if (rows, cols) != (9, 9):
        raise ValueError(f'Wrong board size: ({rows}, {cols})')

    # Auxiliary array to keep track of fixed and temporary cells
    # 0: not in use
    # 1: temporary cell for current solution
    # 2: fixed cell
    status = [[0] * cols for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            if board[row][col] > 0:
                status[row][col] = 2

    # Begin solution from top left corner
    return rec_solve(board, status, 0, 0)


def rec_solve(board, status, row, col):
    if row == rows:  # we have reached the end
        count = 0  # count and check if all cells are occupied
        for r in range(rows):
            for c in range(cols):
                if board[r][c] >= 1:
                    count += 1
        if count == rows * cols:  # board is full, we have a solution
            return board
        else:
            return "NO SOLUTION"

    if status[row][col] >= 1:  # current cell already occupied, proceed to next
        next_row, next_col = next_position(row, col)
        return rec_solve(board, status, next_row, next_col)

    # Cell is empty and we can attempt bruteforce

    candidates = set(range(1, 10))

    # Check row
    for c in range(cols):
        remove_candidate(board[row][c], candidates)

    # Check column
    for r in range(rows):
        remove_candidate(board[r][col], candidates)

    # Find top left corner of box
    row_offset = find_offset(row)  # 0, 3, or 6
    col_offset = find_offset(col)  # 0, 3, or 6

    # Check box
    for r in range(3):
        for c in range(3):
            remove_candidate(board[r + row_offset][c + col_offset], candidates)

    # Test every candidate in the current position, return first found solution
    for candidate in candidates:
        status[row][col] = 1
        board[row][col] = candidate

        next_row, next_col = next_position(row, col)
        solution = rec_solve(board, status, next_row, next_col)

        # Return the solution if it worked
        if solution != "NO SOLUTION":
            return solution

        # Candidate made board unsolvable, roll back cells ahead of us
        ri, ci = row, col
        while (ri, ci) != (9, 0):
            if status[ri][ci] == 1:
                status[ri][ci] = 0
                board[ri][ci] = 0
            ri, ci = next_position(ri, ci)

    # If no candidates exist or none solved the board
    return "NO SOLUTION"


# Auxiliary function to avoid dealing with KeyError from set.remove function
def remove_candidate(candidate, candidate_set: set):
    try:
        candidate_set.remove(candidate)
    except KeyError:
        pass


# Auxiliary function to find the top left corner of the current box
def find_offset(sequence_number):
    if sequence_number in [0, 1, 2]:
        return 0
    if sequence_number in [3, 4, 5]:
        return 3
    if sequence_number in [6, 7, 8]:
        return 6


# Auxiliary function to increment the current position
def next_position(row, col):
    col += 1
    if col >= cols:
        col = 0
        row += 1
    return row, col
