import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countBattleships(test_input)

    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == 'X' and (i == 0 or board[i - 1][j] != 'X') and (j == 0 or board[i][j - 1] != 'X'):
                    ans += 1
        return ans
