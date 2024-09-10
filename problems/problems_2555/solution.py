import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximizeWin(*test_input)

    def maximizeWin(self, prizePositions: List[int], k: int) -> int:
        ans = 0
        max_pick = [0] * (len(prizePositions) + 1)
        left = 0
        for right, p in enumerate(prizePositions):
            while prizePositions[left] < p - k:
                left += 1
            ans = max(ans, max_pick[left] + right - left + 1)
            max_pick[right + 1] = max(max_pick[right],  right - left + 1)
        return ans
