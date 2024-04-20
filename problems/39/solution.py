import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.combinationSum(*test_input)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        path = []

        def dfs(x, s):
            if s == 0:
                ans.append(list(path))
                return
            if x < 0 or s < 0:
                return
            # 不选当前
            dfs(x - 1, s)
            # 选当前
            path.append(candidates[x])
            dfs(x, s - candidates[x])
            path.pop()
        
        dfs(len(candidates) - 1, target)
        return ans
