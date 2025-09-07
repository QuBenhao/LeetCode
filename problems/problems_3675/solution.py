import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(test_input)

    def minOperations(self, s: str) -> int:
        ans = 0
        counter = [0] * 26
        for c in s:
            counter[ord(c) - ord('a')] += 1
        for i in range(1, 25):
            if counter[i]:
                ans += 1
            counter[i + 1] += counter[i]
        ans += 1 if counter[25] > 0 else 0
        return ans
