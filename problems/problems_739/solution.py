import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.dailyTemperatures(test_input)

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans
