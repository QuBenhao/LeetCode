import solution
from typing import *
from functools import lru_cache
from math import inf
from itertools import product


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.cherryPickup(test_input)

    def cherryPickup(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        @lru_cache(None)
        def dfs(step, i1, i2):
            if step == m + n - 2:
                return grid[-1][-1]
            if i1 > i2:
                return dfs(step, i2, i1)
            ans = -inf
            nxt_i1, nxt_i2 = [], []
            if i1 < m - 1 and grid[i1 + 1][step - i1] != -1:
                nxt_i1.append(i1 + 1)
            if step - i1 < n - 1 and grid[i1][step - i1 + 1] != -1:
                nxt_i1.append(i1)
            if i2 < m - 1 and grid[i2 + 1][step - i2] != -1:
                nxt_i2.append(i2 + 1)
            if step - i2 < n - 1 and grid[i2][step - i2 + 1] != -1:
                nxt_i2.append(i2)
            for ni1, ni2 in product(nxt_i1, nxt_i2):
                ans = max(ans, dfs(step + 1, ni1, ni2))
            return ans + (grid[i1][step - i1] + grid[i2][step - i2] if i1 != i2 else grid[i1][step - i1]) if ans != -inf else ans
        
        ans = dfs(0, 0, 0)
        return 0 if ans == -inf else ans
