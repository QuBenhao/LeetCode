from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxFrequency(*test_input)

    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        counts = defaultdict(int)
        diff = defaultdict(int)
        for num in nums:
            counts[num] += 1
            diff[num] += 0
            diff[num - k] += 1
            diff[num + k + 1] -= 1
        ans = sum_d = 0
        for x, d in sorted(diff.items()):
            sum_d += d
            ans = max(ans, min(sum_d, counts[x] + numOperations))
        return ans
