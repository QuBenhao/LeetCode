from collections import deque
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSubArrayLen(*test_input)

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        q = deque()
        cur_sum = 0
        ans = inf
        for num in nums:
            q.append(num)
            cur_sum += num
            while cur_sum >= target:
                ans = min(ans, len(q))
                cur_sum -= q.popleft()
        return ans if ans != inf else 0
