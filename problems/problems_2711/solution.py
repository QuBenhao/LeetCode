import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.differenceOfDistinctValues(test_input)

    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * n for _ in range(m)]

        for k in range(1, m + n):
            min_j = max(n - k, 0)
            max_j = min(m + n - 1 - k, n - 1)

            st = 0
            for j in range(min_j, max_j + 1):
                i = k + j - n
                ans[i][j] = st.bit_count()  # 计算 st 中 1 的个数
                st |= 1 << grid[i][j]  # 把 grid[i][j] 加到 st 中

            st = 0
            for j in range(max_j, min_j - 1, -1):
                i = k + j - n
                ans[i][j] = abs(ans[i][j] - st.bit_count())
                st |= 1 << grid[i][j]
        return ans
