from functools import cache
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.concatenatedDivisibility(*test_input)

    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        nums.sort()
        pow10 = [10 ** len(str(num)) for num in nums]
        ans = []

        @cache
        def dfs(s, x) -> bool: # Bit i of s is 1 if nums[i] has not been used; x is the current remainder
            if s == 0:
                return x == 0
            for i, (p10, num) in enumerate(zip(pow10, nums)): # Iterate in order, preferring smaller numbers first
                if (s >> i) & 1 and dfs(s ^ (1 << i), (x * p10 + num) % k): # Incorporate the previous remainder here; multiplying by the current pow10 shifts it to the left
                    ans.append(num)
                    return True
            return False
        
        if dfs((1 << n) - 1, 0):
            return ans[::-1]
        return []
