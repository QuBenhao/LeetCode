from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxFreqSum(test_input)

    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"
        counter1, counter2 = defaultdict(int), defaultdict(int)
        get_counter = lambda _c: counter1 if _c in vowels else counter2
        for c in s:
            get_counter(c)[c] += 1
        return max(counter1.values(), default=0) + max(counter2.values(), default=0)
