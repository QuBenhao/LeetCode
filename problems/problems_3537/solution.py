import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.specialGrid(test_input)

    def specialGrid(self, N: int) -> List[List[int]]:
        # 2 ** N
        n = 1 << N
        ans = [[0] * n for _ in range(n)]

        def dfs(start, left, row, length):
            if length == 1:
                ans[row][left] = start
                return start + 1
            lh = left + (length // 2)
            rh = row + (length // 2)
            nxt = dfs(start, lh, row, length // 2)
            nxt = dfs(nxt, lh, rh, length // 2)
            nxt = dfs(nxt, left, rh, length // 2)
            return dfs(nxt, left, row, length // 2)

        dfs(0, 0, 0, n)
        return ans
