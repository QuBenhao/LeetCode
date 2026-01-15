from itertools import combinations

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximizeSquareArea(*test_input)

    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences.extend([1, m])
        vFences.extend([1, n])
        ans_d = 0
        s1 = set()
        for a, b in combinations(hFences, 2):
            s1.add(abs(a - b))
        for a, b in combinations(vFences, 2):
            if (d := abs(a - b)) > ans_d and d in s1:
                ans_d = d

        return ans_d * ans_d % MOD if ans_d > 0 else -1

MOD = int(1e9) + 7
