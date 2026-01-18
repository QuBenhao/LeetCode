import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.bestTower(*test_input)

    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        ans, ans_p = None, -1
        cx, cy = center
        for x, y, q in towers:
            if abs(x-cx)+abs(y-cy) > radius:
                continue
            if q > ans_p:
                ans, ans_p = (x, y), q
            elif q == ans_p:
                ans = min(ans, (x, y))
        return list(ans) if ans else [-1, -1]
