from collections import deque, defaultdict
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minLength(*test_input)

    def minLength(self, nums: List[int], k: int) -> int:
        window = deque()
        ws = defaultdict(int)
        cur = 0
        ans = inf
        for num in nums:
            window.append(num)
            if ws[num] == 0:
                cur += num
            ws[num] += 1
            while window and cur >= k:
                ans = min(ans, len(window))
                v = window.popleft()
                ws[v] -= 1
                if ws[v] == 0:
                    cur -= v
        return ans if ans != inf else -1
