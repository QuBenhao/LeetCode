from collections import defaultdict
from math import inf
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countCoveredBuildings(*test_input)

    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        counter_x = defaultdict(lambda: [inf, -inf])
        counter_y = defaultdict(lambda: [inf, -inf])
        for x, y in buildings:
            counter_x[x][0] = min(counter_x[x][0], y)
            counter_x[x][1] = max(counter_x[x][1], y)
            counter_y[y][0] = min(counter_y[y][0], x)
            counter_y[y][1] = max(counter_y[y][1], x)
        ans = 0
        for x, y in buildings:
            if counter_x[x][0] < y < counter_x[x][1] and counter_y[y][0] < x < counter_y[y][1]:
                ans += 1
        return ans
