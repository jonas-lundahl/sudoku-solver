class SudokuSolver:

    ROWS = 9
    COLS = 9
    NO_SOLUTION = "NO SOLUTION"

    def solve(self, board):
        """
        Solves a given Sudoku board of type list[list[int]].
        Board must have 9 rows and 9 columns.
        """

        if not isinstance(board, list):
            raise TypeError(f'Not a board: {board}')
        if not board:
            raise ValueError(f'Empty board: {board}')

        rows = len(board)
        cols = len(board[0])

        if (rows, cols) != (self.ROWS, self.COLS):
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
        return self.__solve(board, status, 0, 0)

    def __solve(self, board, status, row, col):
        """
        Solves the sudoku board using recursion.
        """

        if row == self.ROWS:  # we have reached the end
            count = 0  # count and check if all cells are occupied
            for r in range(self.ROWS):
                for c in range(self.COLS):
                    if board[r][c] >= 1:
                        count += 1
            if count == self.ROWS * self.COLS:  # board is full, we have a solution
                return board
            else:
                return self.NO_SOLUTION

        if status[row][col] >= 1:  # current cell already occupied, proceed to next
            next_row, next_col = self.__next_position(row, col)
            return self.__solve(board, status, next_row, next_col)

        # Cell is empty and we can attempt bruteforce

        candidates = set(range(1, 10))

        # Check row
        for c in range(self.COLS):
            self.__remove_candidate(board[row][c], candidates)

        # Check column
        for r in range(self.ROWS):
            self.__remove_candidate(board[r][col], candidates)

        # Find top left corner of box
        row_offset = self.__find_offset(row)  # 0, 3, or 6
        col_offset = self.__find_offset(col)  # 0, 3, or 6

        # Check box
        for r in range(3):
            for c in range(3):
                cell = board[r + row_offset][c + col_offset]
                self.__remove_candidate(cell, candidates)

        # Test every candidate in the current position, return first found solution
        for candidate in candidates:
            status[row][col] = 1
            board[row][col] = candidate

            next_row, next_col = self.__next_position(row, col)
            solution = self.__solve(board, status, next_row, next_col)

            # Return the solution if it worked
            if solution != self.NO_SOLUTION:
                return solution

            # Candidate made board unsolvable, roll back cells ahead of us
            ri, ci = row, col
            while (ri, ci) != (9, 0):
                if status[ri][ci] == 1:
                    status[ri][ci] = 0
                    board[ri][ci] = 0
                ri, ci = self.__next_position(ri, ci)

        # If no candidates exist or none solved the board
        return self.NO_SOLUTION

    def __remove_candidate(self, candidate, candidate_set: set):
        """
        Auxiliary method to avoid dealing with KeyError from set.remove method.
        """

        try:
            candidate_set.remove(candidate)
        except KeyError:
            pass

    def __find_offset(self, sequence_number):
        """
        Auxiliary method to find the top left corner of the current box.
        """

        if sequence_number in [0, 1, 2]:
            return 0
        if sequence_number in [3, 4, 5]:
            return 3
        if sequence_number in [6, 7, 8]:
            return 6

    def __next_position(self, row, col):
        """
        Auxiliary method to increment the current position on the board.
        """
        col += 1
        if col >= self.COLS:
            col = 0
            row += 1
        return row, col
