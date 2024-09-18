import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.dailyTemperatures(test_input)

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                pre = stack.pop()
                ans[pre] = i - pre
            stack.append(i)
        return ans
