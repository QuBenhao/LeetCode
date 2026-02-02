from math import inf

from sortedcontainers import SortedList

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumCost(*test_input)

    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        sl = SortedList()
        ans = inf
        s = 0
        n = len(nums)
        k -= 1
        for i in range(1, n):
            # 如果进入前k小
            if len(sl) >= k and nums[i] < sl[k - 1]:
                s += nums[i] - sl[k - 1]
            elif len(sl) < k:
                s += nums[i]
            sl.add(nums[i])
            if i > dist + 1:
                sl.remove(nums[i - dist - 1])
                # 如果删除的是前k小
                if nums[i - dist - 1] < sl[k - 1]:
                    s += sl[k - 1] - nums[i - dist - 1]
            if i >= k:
                ans = min(ans, s)
        return ans + nums[0]
