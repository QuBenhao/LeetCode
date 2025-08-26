from itertools import combinations

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.validSquare(*test_input)

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(point1, point2):
            return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

        distances = list(sorted(distance(a, b) for a, b in combinations([p1, p2, p3, p4], 2)))
        return distances[0] > 0 and distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == \
            distances[5] and distances[4] == 2 * distances[0]
