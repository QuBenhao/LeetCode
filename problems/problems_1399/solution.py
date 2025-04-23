from collections import defaultdict
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countLargestGroup(test_input)

    def countLargestGroup(self, n: int) -> int:
        counter = defaultdict(int)
        for i in range(1, n + 1):
            cur, s = i, 0
            while cur:
                s += cur % 10
                cur //= 10
            counter[s] += 1
        ans, m = 0, 0
        for v in counter.values():
            if v > m:
                ans = 1
                m = v
            elif v == m:
                ans += 1
        return ans
