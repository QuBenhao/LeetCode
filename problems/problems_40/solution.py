import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.combinationSum2(*test_input)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        candidates.sort()
        n = len(candidates)

        def backtrack(idx, remain):
            if remain < 0:
                return
            if not remain:
                ans.append(list(path))
                return
            if idx == n:
                return
            path.append(candidates[idx])
            backtrack(idx + 1, remain - candidates[idx])
            path.pop()
            nxt = idx + 1
            while nxt < n and candidates[nxt] == candidates[nxt - 1]:
                nxt += 1
            backtrack(nxt, remain)

        backtrack(0, target)
        return ans
