import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.distanceBetweenBusStops(*test_input)

    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        n = len(distance)
        distance += distance
        clock = 0
        for i in range(start, destination if destination > start else destination + n):
            clock += distance[i]
        clockwise = 0
        for i in range(destination, start if start > destination else start + n):
            clockwise += distance[i]
        return min(clock, clockwise)
