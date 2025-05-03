from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minDominoRotations(*test_input)

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        tp, bt =  tops[0], bottoms[0]
        ans1 = ans2 = 0
        ans3 = ans4 = 0
        for t, b in zip(tops, bottoms):
            if t != tp and b != tp:
                ans1 = inf
                ans3 = inf
            else:
                if t != tp:
                    ans1 += 1
                if b != tp:
                    ans3 += 1
            if t != bt and b != bt:
                ans2 = inf
                ans4 = inf
            else:
                if b != bt:
                    ans2 += 1
                if t != bt:
                    ans4 += 1
            if ans1 == ans2 == ans3 == ans4 == inf:
                break
        return -1 if (a := min(ans1, ans2, ans3, ans4)) == inf else a
