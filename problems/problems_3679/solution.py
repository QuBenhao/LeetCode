from collections import deque, defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minArrivalsToDiscard(*test_input)

    def minArrivalsToDiscard(self, arrivals: List[int], w: int, m: int) -> int:
        counter = defaultdict(int)
        window = deque()
        ans = 0
        for i, v in enumerate(arrivals):
            while window and window[0] < i - w + 1:
                counter[arrivals[window.popleft()]] -= 1
            counter[v] += 1
            if counter[v] > m:
                counter[v] -= 1
                ans += 1
            else:
                window.append(i)
        return ans
