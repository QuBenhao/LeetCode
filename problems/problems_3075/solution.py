import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumHappinessSum(*test_input)

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0
        for i in range(k):
            if happiness[i] <= i:
                break
            ans += happiness[i] - i
        return ans
