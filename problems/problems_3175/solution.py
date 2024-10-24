import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findWinningPlayer(*test_input)

    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        ans = cur = 0
        for i in range(1, len(skills)):
            if skills[i] < skills[ans]:
                cur += 1
            else:
                cur = 1
                ans = i
            if cur == k:
                return ans
        return ans
