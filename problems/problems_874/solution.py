import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.robotSim(*test_input)

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles_ = set(map(tuple, obstacles))
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = d = ans = 0

        for c in commands:
            if c < 0:
                d = (d + (1 if c == -1 else 3)) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(c):
                    if (x + dx, y + dy) in obstacles_:
                        break
                    x, y = x + dx, y + dy
                ans = max(ans, x * x + y * y)
        return ans
