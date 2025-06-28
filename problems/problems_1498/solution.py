import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numSubseq(*test_input)

    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, n - 1
        ans = 0
        powers = [1] * n
        for i in range(1, n):
            powers[i] = (powers[i - 1] * 2) % MOD
        while left <= right:
            while right >= left and nums[right] + nums[left] > target:
                right -= 1
            if right < left:
                break
            ans = (ans + powers[right - left]) % MOD
            left += 1
        return ans

MOD = 10**9 + 7
