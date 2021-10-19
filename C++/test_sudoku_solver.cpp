#include "gtest/gtest.h"
#include "sudoku_solver.h"

// The fixture for testing class SudokuSolver.
class SudokuSolverTest : public ::testing::Test {
   protected:
    SudokuSolver solver;
    void SetUp() override { solver = SudokuSolver(); }
};

TEST_F(SudokuSolverTest, SolveOneTile) {
    board_t board = {{{4, 3, 5, 2, 6, 9, 7, 8, 1},
                      {6, 0, 2, 5, 7, 1, 4, 9, 3},  // 2nd column should be 8
                      {1, 9, 7, 8, 3, 4, 5, 6, 2},
                      {8, 2, 6, 1, 9, 5, 3, 4, 7},
                      {3, 7, 4, 6, 8, 2, 9, 1, 5},
                      {9, 5, 1, 7, 4, 3, 6, 2, 8},
                      {5, 1, 9, 3, 2, 6, 8, 7, 4},
                      {2, 4, 8, 9, 5, 7, 1, 3, 6},
                      {7, 6, 3, 4, 1, 8, 2, 5, 9}}};
    solver.setBoard(board);
    solver.solveBoard();
    board[1][1] = 8;
    board_t result = solver.getBoard();
    EXPECT_EQ(board, result);
}

TEST_F(SudokuSolverTest, SolveEmptyBoard) {
    board_t board = {};
    solver.setBoard(board);
    solver.solveBoard();
    board = {{{1, 2, 3, 4, 5, 6, 7, 8, 9},
              {4, 5, 6, 7, 8, 9, 1, 2, 3},
              {7, 8, 9, 1, 2, 3, 4, 5, 6},
              {2, 1, 4, 3, 6, 5, 8, 9, 7},
              {3, 6, 5, 8, 9, 7, 2, 1, 4},
              {8, 9, 7, 2, 1, 4, 3, 6, 5},
              {5, 3, 1, 6, 4, 2, 9, 7, 8},
              {6, 4, 2, 9, 7, 8, 5, 3, 1},
              {9, 7, 8, 5, 3, 1, 6, 4, 2}}};
    board_t result = solver.getBoard();
    EXPECT_EQ(board, result);
}

TEST_F(SudokuSolverTest, SolveNormalBoard) {
    board_t board = {{{0, 2, 0, 0, 0, 0, 0, 0, 0},
                      {0, 0, 0, 6, 0, 0, 0, 0, 3},
                      {0, 7, 4, 0, 8, 0, 0, 0, 0},
                      {0, 0, 0, 0, 0, 3, 0, 0, 2},
                      {0, 8, 0, 0, 4, 0, 0, 1, 0},
                      {6, 0, 0, 5, 0, 0, 0, 0, 0},
                      {0, 0, 0, 0, 1, 0, 7, 8, 0},
                      {5, 0, 0, 0, 0, 9, 0, 0, 0},
                      {0, 0, 0, 0, 0, 0, 0, 4, 0}}};

    board_t expected = {{{1, 2, 6, 4, 3, 7, 9, 5, 8},
                         {8, 9, 5, 6, 2, 1, 4, 7, 3},
                         {3, 7, 4, 9, 8, 5, 1, 2, 6},
                         {4, 5, 7, 1, 9, 3, 8, 6, 2},
                         {9, 8, 3, 2, 4, 6, 5, 1, 7},
                         {6, 1, 2, 5, 7, 8, 3, 9, 4},
                         {2, 6, 9, 3, 1, 4, 7, 8, 5},
                         {5, 4, 8, 7, 6, 9, 2, 3, 1},
                         {7, 3, 1, 8, 5, 2, 6, 4, 9}}};

    solver.setBoard(board);
    solver.solveBoard();
    board_t actual = solver.getBoard();
    EXPECT_EQ(expected, actual);
}

TEST_F(SudokuSolverTest, SolveImpossible) {
    board_t board = {{{5, 1, 6, 8, 4, 9, 7, 3, 2},
                      {3, 0, 7, 6, 0, 5, 0, 0, 0},
                      {8, 0, 9, 7, 0, 0, 0, 6, 5},
                      {1, 3, 5, 0, 6, 0, 9, 0, 7},
                      {4, 7, 2, 5, 9, 1, 0, 0, 6},
                      {9, 6, 8, 3, 7, 0, 0, 5, 0},
                      {2, 5, 3, 1, 8, 6, 0, 7, 4},
                      {6, 8, 4, 2, 0, 7, 5, 0, 0},
                      {7, 9, 1, 0, 5, 0, 6, 0, 8}}};
    solver.setBoard(board);
    EXPECT_FALSE(solver.solveBoard());
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}