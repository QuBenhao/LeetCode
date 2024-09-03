import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.combinationSum(*test_input)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, target):
            if target == 0:
                ans.append(path[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i, path, target - candidates[i])
                path.pop()

        ans = []
        candidates.sort()
        backtrack(0, [], target)
        return ans
