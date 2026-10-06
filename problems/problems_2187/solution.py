import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumTime(*test_input)

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        min_t = min(time)
        avg = (totalTrips - 1) // len(time) + 1
        left = min_t * avg - 1  # Loop invariant: sum >= totalTrips is always False
        right = min(max(time) * avg, min_t * totalTrips)  # Loop invariant: sum >= totalTrips is always True
        while left + 1 < right:  # The open interval (left, right) is nonempty
            mid = (left + right) // 2
            if sum(mid // t for t in time) >= totalTrips:
                right = mid  # Shrink the binary-search interval to (left, mid)
            else:
                left = mid  # Shrink the binary-search interval to (mid, right)
        # Now left equals right-1
        # sum(left) < totalTrips and sum(right) >= totalTrips, so the answer is right
        return right
