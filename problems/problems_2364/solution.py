from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countBadPairs(test_input)

    def countBadPairs(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for i, num in enumerate(nums):
            count[num - i] += 1
        ans = 0
        n = len(nums)
        for v in count.values():
            ans += v * (n - v)
        return ans // 2
