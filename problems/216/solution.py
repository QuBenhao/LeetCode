import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.combinationSum3(*test_input)

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def dfs(path, cur, remain, picks):
            if remain == 0 and not picks:
                ans.append(list(path))
                return
            if not picks or not cur:
                return
            for num in range(min(cur, remain), 0, -1):
                path.append(num)
                dfs(path, num - 1, remain - num, picks - 1)
                path.pop()

        dfs([], 9, n, k)
        return ans
