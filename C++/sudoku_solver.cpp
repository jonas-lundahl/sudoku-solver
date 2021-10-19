#include "sudoku_solver.h"

// Auxiliary print function for debugging
std::ostream& operator<<(std::ostream& os, const board_t& board) {
    for (uc row = 0; row < N; row++) {
        for (uc col = 0; col < N; col++) {
            os << board[row][col] << " ";
        }
        os << "\n";
    }
    return os;
}

void SudokuSolver::setBoard(board_t b) { board = b; }

board_t& SudokuSolver::getBoard() { return board; }

bool SudokuSolver::solveBoard() {
    fixed = {};
    for (uc row = 0; row < N; row++) {
        for (uc col = 0; col < N; col++) {
            fixed[row][col] = board[row][col] > 0 ? 2 : 0;
        }
    }

    return solve(0, 0);
}

bool SudokuSolver::solve(uc row, uc col) {
    if (row == N) return true;  // end of board reached

    uc next_row, next_col;
    if (col == 8) {
        next_row = row + 1;
        next_col = 0;
    } else {
        next_row = row;
        next_col = col + 1;
    }

    if (fixed[row][col] == 2)
        return solve(next_row, next_col);  // already occupied

    // Test all possibilities
    for (uc candidate = 1; candidate <= N; candidate++) {
        uc d;

        // Check rows
        for (d = 0; d < N; ++d) {
            if (board[d][col] == candidate) break;
        }
        if (d < N) continue;

        // Check cols
        for (d = 0; d < N; ++d) {
            if (board[row][d] == candidate) break;
        }
        if (d < N) continue;

        // Check box
        uc brow, bcol;  // top left corner of current box
        brow = row / N_BOX * N_BOX;
        bcol = col / N_BOX * N_BOX;
        d = 0;
        for (uc r = 0; r < N_BOX; r++) {
            for (uc c = 0; c < N_BOX; c++) {
                if (board[brow + r][bcol + c] == candidate) break;
                d++;
            }
        }
        if (d < N) continue;

        // Candidate can be placed
        fixed[row][col] = 1;
        board[row][col] = candidate;

        if (solve(next_row, next_col)) {
            return true;
        } else {  // solution failed, restore board
            fixed[row][col] = 0;
            board[row][col] = 0;
        }
    }

    return false;
}
