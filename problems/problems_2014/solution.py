from collections import Counter
from itertools import permutations

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestSubsequenceRepeatedK(*test_input)

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        # x * k <= n < 8 * k
        # x < 8
        def is_sub_sequence(_s, _seq):
            it = iter(_s)
            return all(c in it for c in _seq)

        counter = Counter(s)
        a = [c for c, freq in counter.items() for _ in range(freq // k)]
        a.sort(reverse=True)
        for i in range(len(a), 0, -1):
            for perm in permutations(a, i):
                seq = "".join(perm)
                if is_sub_sequence(s, seq * k):
                    return seq
        return ""
