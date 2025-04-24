from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countInterestingSubarrays(*test_input)

    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        pre_sum = [0] * (n + 1)
        for i, num in enumerate(nums):
            pre_sum[i + 1] = pre_sum[i] + (num % modulo == k)
        ans = 0
        counter = defaultdict(int)
        counter[0] = 1
        for i in range(1, n + 1):
            target = (pre_sum[i] - k + modulo) % modulo
            ans += counter[target]
            counter[pre_sum[i] % modulo] += 1
        return ans
