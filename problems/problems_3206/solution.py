import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfAlternatingGroups(test_input)

    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        ans, n = 0, len(colors)
        for i in range(n):
            if colors[i] != colors[i - 1] and colors[i] != colors[(i + 1) % n]:
                ans += 1
        return ans
