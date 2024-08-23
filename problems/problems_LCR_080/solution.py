import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.combine(*test_input)

    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def backtrack(cur: int, path: List[int]):
            if len(path) == k:
                ans.append(path[:])
                return
            for i in range(cur, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()

        backtrack(1, [])
        return ans
