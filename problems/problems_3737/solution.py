import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countMajoritySubarrays(*test_input)

    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            cnt =0
            for j in range(i, n):
                if nums[j] == target:
                    cnt += 1
                if cnt * 2 > j - i + 1:
                    ans += 1
        return ans

