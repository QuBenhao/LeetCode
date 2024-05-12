import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.garbageCollection(*test_input)

    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        ans = len(garbage[0])
        seen = set()
        for g, t in zip(reversed(garbage), reversed(travel)):
            seen.update(g)
            ans += len(g) + t * len(seen)
        return ans
