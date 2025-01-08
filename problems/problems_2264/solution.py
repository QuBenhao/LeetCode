import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestGoodInteger(test_input)

    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        for i in range(len(num) - 2):
            if ans and num[i] < ans[0]:
                continue
            if num[i] == num[i + 1] == num[i + 2]:
                ans = num[i:i + 3]
        return ans
