from bisect import bisect_left
from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxSubstrings(test_input)

    def maxSubstrings(self, word: str) -> int:
        ans = 0
        pos = {}
        for i, c in enumerate(word):
            if c not in pos:
                pos[c] = i
            elif i - pos[c] > 2:
                # 右端点越小越好，找到就清除
                ans += 1
                pos.clear()
        return ans
