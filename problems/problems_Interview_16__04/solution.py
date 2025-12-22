import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.tictactoe(test_input)

    def tictactoe(self, board: List[str]) -> str:
        n = len(board)
        if board[0][0] != ' ' and all(board[i][i] == board[0][0] for i in range(n)):
            return board[0][0]
        if board[0][-1] != ' ' and all(board[i][-1-i] == board[0][-1] for i in range(n)):
            return board[0][-1]
        unfill = False
        row_count_o, row_count_x = [0] * n, [0] * n
        col_count_o, col_count_x = [0] * n, [0] * n
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                match c:
                    case 'X':
                        row_count_x[i] += 1
                        col_count_x[j] += 1
                        if j == n - 1 and row_count_x[i] == n:
                            return c
                        if i == n - 1 and col_count_x[j] == n:
                            return c
                    case 'O':
                        row_count_o[i] += 1
                        col_count_o[j] += 1
                        if j == n - 1 and row_count_o[i] == n:
                            return c
                        if i == n - 1 and col_count_o[j] == n:
                            return c
                    case _:
                        unfill = True
        return 'Pending' if unfill else 'Draw'
