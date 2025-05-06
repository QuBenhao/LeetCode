import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numRookCaptures(test_input)

    def numRookCaptures(self, board: List[List[str]]) -> int:
        m, n = len(board), len(board[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = -1
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v == 'R':
                    x, y = i, j
                    break
            if x != -1:
                break
        ans = 0
        for d in dirs:
            cur_x, cur_y = x, y
            while True:
                nx, ny = cur_x + d[0], cur_y + d[1]
                if nx < 0 or nx == m or ny < 0 or ny == n:
                    break
                if board[nx][ny] == 'B':
                    break
                if board[nx][ny] == 'p':
                    ans += 1
                    break
                cur_x, cur_y = nx, ny
        return ans

