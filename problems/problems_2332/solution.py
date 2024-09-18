import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.latestTimeCatchTheBus(*test_input)

    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        ans = -1
        buses.sort()
        passengers.sort()
        n = len(passengers)
        j = 0
        for t in buses:
            c = capacity
            while c and j < n and passengers[j] <= t:
                c -= 1
                j += 1
        j -= 1
        ans = buses[-1] if c else passengers[j]
        while j >= 0 and ans == passengers[j]:
            ans -= 1
            j -= 1
        return ans
