from bisect import bisect_left

from math import inf

import solution
from collections import Counter
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumDeletions(*test_input)

    def minimumDeletions(self, word: str, k: int) -> int:
        counter = Counter(word)
        values = sorted(counter.values())
        n = len(values)
        ans = len(word)
        for i, v in enumerate(values):
            if i > 0 and values[i - 1] == v:
                continue
            cur, min_d, max_d = 0, v, v + k
            for j in range(i):
                if values[j] >= min_d:
                    break
                cur += values[j]
            for j in range(n - 1, i, -1):
                if values[j] <= max_d:
                    break
                cur += values[j] - max_d
            ans = min(ans, cur)
        return ans
