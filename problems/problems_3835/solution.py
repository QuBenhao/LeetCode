from collections import deque

from sortedcontainers import SortedList

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countSubarrays(*test_input)

    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        sl = SortedList()
        window = deque()
        for num in nums:
            sl.add(num)
            window.append(num)
            while sl and (sl[-1] - sl[0]) * len(sl) > k:
                sl.discard(window.popleft())
            ans += len(sl)
        return ans
