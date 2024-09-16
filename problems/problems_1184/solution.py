import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.distanceBetweenBusStops(*test_input)

    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        return min(sum(distance) - s, s) if (s := sum(distance[min(start, destination):max(start, destination)])) >= 0 else 0
