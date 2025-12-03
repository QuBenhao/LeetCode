import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countCollisions(test_input)

    def countCollisions(self, directions: str) -> int:
        ans = 0
        r = 0
        has_stop = False
        for d in directions:
            if d == 'R':
                r += 1
            else:
                ans += r
                if r and d == 'L':
                    ans += 1
                elif has_stop and d == 'L':
                    ans += 1
                has_stop = has_stop or r > 0 or d == 'S'
                r = 0
        return ans
