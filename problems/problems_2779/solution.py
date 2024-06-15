import solution
from typing import *
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumBeauty(*test_input)

    def maximumBeauty(self, nums: List[int], k: int) -> int:
        diffs = defaultdict(int)
        for num in nums:
            diffs[num - k] += 1
            diffs[num + k + 1] -= 1
        ans = cur = 0
        for _, v in sorted(diffs.items()):
            cur += v
            ans = max(ans, cur)
        return ans
