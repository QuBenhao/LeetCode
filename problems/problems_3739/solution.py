from sortedcontainers import SortedList

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countMajoritySubarrays(*test_input)

    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        sl = SortedList([0])  # 为什么加个 0？见 525 题我的题解
        ans = s = 0
        for x in nums:
            s += 1 if x == target else -1
            ans += sl.bisect_left(s)
            sl.add(s)
        return ans
