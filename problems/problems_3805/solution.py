from collections import defaultdict
from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countPairs(test_input)

    def countPairs(self, words: List[str]) -> int:
        def _hash(s: str):
            res = ""
            for a, b in pairwise(s):
                res += str((ord(b) - ord(a)) % 26) + ","
            return res

        ans = 0
        counter = defaultdict(int)
        for word in words:
            h = _hash(word)
            ans += counter[h]
            counter[h] += 1
        return ans
