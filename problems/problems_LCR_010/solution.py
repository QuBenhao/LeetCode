import solution
from typing import *
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.subarraySum(*test_input)

    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        ans, pre_sum = 0, 0
        for num in nums:
            pre_sum += num
            ans += count[pre_sum - k]
            count[pre_sum] += 1
        return ans
