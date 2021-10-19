#include "sudoku_solver.h"

#include "bits/stdc++.h"

using namespace std;

// Auxiliary print function for debugging
ostream& operator<<(ostream& os, const board_t& board) {
    for (size_t row = 0; row < 9; row++) {
        for (size_t col = 0; col < 9; col++) {
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
    for (size_t row = 0; row < 9; row++) {
        for (size_t col = 0; col < 9; col++) {
            fixed[row][col] = board[row][col] > 0 ? 2 : 0;
        }
    }

    return solve(0, 0);
}

bool SudokuSolver::solve(int row, int col) {
    if (row == 9) return true;  // end of board reached

    int next_row, next_col;
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
    for (int candidate = 1; candidate <= 9; candidate++) {
        int d;

        // Check rows
        for (d = 0; d < 9; ++d) {
            if (board[d][col] == candidate) break;
        }
        if (d < 9) continue;

        // Check cols
        for (d = 0; d < 9; ++d) {
            if (board[row][d] == candidate) break;
        }
        if (d < 9) continue;

        // Check box
        int brow, bcol;  // top left corner of current box
        brow = row / 3 * 3;
        bcol = col / 3 * 3;
        d = 0;
        for (int r = 0; r < 3; r++) {
            for (int c = 0; c < 3; c++) {
                if (board[brow + r][bcol + c] == candidate) break;
                d++;
            }
        }
        if (d < 9) continue;

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
