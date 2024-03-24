import solution
from typing import *


DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.exist(*test_input)

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def back_tracking(idx, i, j):
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[idx]:
                return False
            if idx == len(word) - 1:
                return True
            board[i][j] = ""
            for dx, dy in DIRS:
                if back_tracking(idx + 1, i + dx, j + dy):
                    return True
            board[i][j] = word[idx]
            return False

        for i in range(m):
            for j in range(n):
                if back_tracking(0, i, j):
                    return True
        return False
