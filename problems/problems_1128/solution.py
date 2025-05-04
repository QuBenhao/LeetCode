from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numEquivDominoPairs(test_input)

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        ans = 0
        counter = defaultdict(int)
        for domino in dominoes:
            d = max(domino) * 10 + min(domino)
            ans += counter[d]
            counter[d] += 1
        return ans
