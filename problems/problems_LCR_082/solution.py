import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.combinationSum2(*test_input)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(remain, path, idx):
            if remain == 0:
                ans.append(list(path))
                return
            if idx == len(candidates) or remain < 0:
                return
            path.append(candidates[idx])
            backtrack(remain - candidates[idx], path, idx + 1)
            path.pop()
            while idx < len(candidates) - 1 and candidates[idx] == candidates[idx + 1]:
                idx += 1
            backtrack(remain, path, idx + 1)
        candidates.sort()
        backtrack(target, [], 0)
        return ans
