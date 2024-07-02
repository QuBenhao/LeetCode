import solution
from typing import *
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.subarraySum(*test_input)

    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = s = 0
        counter = defaultdict(int)
        counter[0] = 1
        for num in nums:
            s += num
            ans += counter[s - k]
            counter[s] += 1
        return ans
