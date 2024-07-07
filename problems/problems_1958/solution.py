import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkMove(*test_input)

    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(0, 1), (1, 1), (1, 0), (-1, 1), (0, -1), (-1, -1), (-1, 0), (1, -1)]
        for dx, dy in directions:
            x, y = rMove + dx, cMove + dy
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] == '.' or board[x][y] == color:
                continue
            while 0 <= x < m and 0 <= y < n and board[x][y] != '.':
                if board[x][y] == color:
                    return True
                x += dx
                y += dy
        return False
