import solution
from typing import *
from collections import defaultdict
from itertools import combinations


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.distinctNames(test_input)

    def distinctNames(self, ideas: List[str]) -> int:
        groups = defaultdict(set)
        for s in ideas:
            groups[s[0]].add(s[1:])
        ans = 0
        for a, b in combinations(groups.values(), 2):
            cannot = len(a & b)
            ans += (len(a) - cannot) * (len(b) - cannot)
        return ans * 2
