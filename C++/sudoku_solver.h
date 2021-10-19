#pragma once

#include <array>
#include <iostream>

#define N (9)
#define N_BOX (3)

typedef unsigned char uc;
typedef std::array<std::array<uc, N>, N> board_t;

class SudokuSolver {
   private:
    /**
     * Represents the Sudoku board that is to be solved.
     */
    board_t board;

    /**
     * Keeps track of fixed and temporary numbers on the board. Fixed and
     * temporary numbers are denoted by 2 and 1, respectively. Empty cells are
     * 0.
     */
    board_t fixed;
    /**
     * Solves the Sudoku board starting from (row, col).
     * @return true if solution was found, otherwise false
     */
    bool solve(uc, uc);

   public:
    /**
     * Sets the Sudoku board that is to be solved.
     * @param board_t the board to solve
     */
    void setBoard(board_t);

    /**
     * Get the Sudoku board contained in this solver.
     * @return the Sudoku board
     */
    board_t& getBoard();

    /**
     * Solves the Sudoku board. Returns true if solution was found, otherwise
     * false.
     */
    bool solveBoard();
};