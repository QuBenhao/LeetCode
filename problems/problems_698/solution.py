import solution
from typing import *
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canPartitionKSubsets(*test_input)

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        line = total // k
        if any(num > line for num in nums):
            return False
        n = len(nums)
        all_picked = (1 << n) - 1

        @lru_cache(None)
        def dfs(state, cur):
            if cur == line:
                if state == all_picked:
                    return True
                cur = 0
            for i in range(n):
                if not (state >> i) & 1 and cur + nums[i] <= line and dfs(state | (1 << i), cur + nums[i]):
                    return True
            return False

        return dfs(0, 0)
