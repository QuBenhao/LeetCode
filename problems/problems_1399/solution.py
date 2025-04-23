from collections import defaultdict
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countLargestGroup(test_input)

    def countLargestGroup(self, n: int) -> int:
        counter = defaultdict(int)
        ans, m = 0, 0
        for i in range(1, n + 1):
            cur, s = i, 0
            while cur:
                s += cur % 10
                cur //= 10
            counter[s] += 1
            if counter[s] > m:
                m = counter[s]
                ans = 1
            elif counter[s] == m:
                ans += 1
        return ans
