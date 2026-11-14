import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numOfSubarrays(test_input)

    def numOfSubarrays(self, arr: list[int]) -> int:
        # 子数组和为奇数 <=> 两端前缀和奇偶性不同
        odd, even, cur, ans = 0, 1, 0, 0
        for x in arr:
            cur ^= x & 1
            ans += even if cur else odd
            odd += cur
            even += 1 - cur
        return ans % (10**9 + 7)

