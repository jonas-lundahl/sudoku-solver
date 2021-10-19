#pragma once

#include <array>

typedef std::array<std::array<int, 9>, 9> board_t;

class SudokuSolver {
   private:
    board_t board;

   public:
    void setBoard(board_t);
    board_t& getBoard();
    bool solveBoard();
};