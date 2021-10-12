from copy import deepcopy
import unittest

from sudoku_solver import solve


class TestStringMethods(unittest.TestCase):

    def test_solve_empty_input(self):
        with self.assertRaises(ValueError):
            solve([])

    def test_solve_invalid_input_string(self):
        with self.assertRaises(TypeError):
            solve("my board")

    def test_solve_invalid_input_wrong_board_size(self):
        with self.assertRaises(ValueError):
            board = [[0] * 8 for _ in range(9)]  # 9x8 grid
            solve(board)

    def test_solve_one_cell(self):
        board = [
            [4, 3, 5, 2, 6, 9, 7, 8, 1],
            [6, 0, 2, 5, 7, 1, 4, 9, 3],  # 2nd column should be 8
            [1, 9, 7, 8, 3, 4, 5, 6, 2],
            [8, 2, 6, 1, 9, 5, 3, 4, 7],
            [3, 7, 4, 6, 8, 2, 9, 1, 5],
            [9, 5, 1, 7, 4, 3, 6, 2, 8],
            [5, 1, 9, 3, 2, 6, 8, 7, 4],
            [2, 4, 8, 9, 5, 7, 1, 3, 6],
            [7, 6, 3, 4, 1, 8, 2, 5, 9]
        ]
        solution = solve(deepcopy(board))
        self.assertIsNotNone(solution)

        board[1][1] = 8

        self.assertEqual(8, solution[1][1], 'Wrong Solution')
        self.assertEqual(board, solution, 'Fixed elements changed')

    def test_solve_empty_board(self):
        board = [[0] * 9 for _ in range(9)]  # 9x9 grid

        expected_solution = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 1, 4, 3, 6, 5, 8, 9, 7],
            [3, 6, 5, 8, 9, 7, 2, 1, 4],
            [8, 9, 7, 2, 1, 4, 3, 6, 5],
            [5, 3, 1, 6, 4, 2, 9, 7, 8],
            [6, 4, 2, 9, 7, 8, 5, 3, 1],
            [9, 7, 8, 5, 3, 1, 6, 4, 2]
        ]

        solution = solve(board)
        self.assertEqual(expected_solution, solution)

    def test_solve_normal_board(self):
        board = [
            [0, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 6, 0, 0, 0, 0, 3],
            [0, 7, 4, 0, 8, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 3, 0, 0, 2],
            [0, 8, 0, 0, 4, 0, 0, 1, 0],
            [6, 0, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 7, 8, 0],
            [5, 0, 0, 0, 0, 9, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 4, 0]
        ]

        expected_solution = [
            [1, 2, 6, 4, 3, 7, 9, 5, 8],
            [8, 9, 5, 6, 2, 1, 4, 7, 3],
            [3, 7, 4, 9, 8, 5, 1, 2, 6],
            [4, 5, 7, 1, 9, 3, 8, 6, 2],
            [9, 8, 3, 2, 4, 6, 5, 1, 7],
            [6, 1, 2, 5, 7, 8, 3, 9, 4],
            [2, 6, 9, 3, 1, 4, 7, 8, 5],
            [5, 4, 8, 7, 6, 9, 2, 3, 1],
            [7, 3, 1, 8, 5, 2, 6, 4, 9]
        ]

        solution = solve(board)
        self.assertEqual(expected_solution, solution)

    def test_solve_impossible(self):
        board = [
            [5, 1, 6, 8, 4, 9, 7, 3, 2],
            [3, 0, 7, 6, 0, 5, 0, 0, 0],
            [8, 0, 9, 7, 0, 0, 0, 6, 5],
            [1, 3, 5, 0, 6, 0, 9, 0, 7],
            [4, 7, 2, 5, 9, 1, 0, 0, 6],
            [9, 6, 8, 3, 7, 0, 0, 5, 0],
            [2, 5, 3, 1, 8, 6, 0, 7, 4],
            [6, 8, 4, 2, 0, 7, 5, 0, 0],
            [7, 9, 1, 0, 5, 0, 6, 0, 8]
        ]
        solution = solve(board)
        self.assertEqual("NO SOLUTION", solution)


if __name__ == '__main__':
    unittest.main()
