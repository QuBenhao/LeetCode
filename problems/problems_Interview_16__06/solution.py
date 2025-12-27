from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallestDifference(*test_input)

    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        ans = inf
        i, j, n, m = 0, 0, len(a), len(b)
        while i < n and j < m:
            ans = min(ans, abs(a[i] - b[j]))
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
        return ans
