import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfAlternatingGroups(*test_input)

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        ans, cnt = 0, 0
        for i in range(1, n + k - 1):
            if colors[i % n] == colors[(i - 1) % n]:
                cnt = 0
            else:
                cnt += 1
            if cnt >= k - 1:
                ans += 1
        return ans
