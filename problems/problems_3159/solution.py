import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.occurrencesOfElement(*test_input)

    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        mp, cnt = {}, 0
        for i, num in enumerate(nums):
            if num == x:
                mp[cnt + 1] = i
                cnt += 1
        return [mp.get(q, -1) for q in queries]
