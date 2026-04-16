import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minMirrorPairDistance(test_input)

    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        def cache_key(x):
            # c = 0
            # while x:
            #     x, r = divmod(x, 10)
            #     c = c * 10 + r
            # return c
            return int(str(x)[::-1])

        mp = {}
        for i, num in enumerate(nums):
            if num in mp:
                ans = min(ans, i - mp[num])
            mp[cache_key(num)] = i
        return ans if ans < n else -1
