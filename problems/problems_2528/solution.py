import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxPower(*test_input)

    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        # Sliding window
        s = sum(stations[:r])  # Compute the power in [0, r-1] to prepare the first window
        power = [0] * n
        for i in range(n):
            # Enter from the right
            if (right := i + r) < n:
                s += stations[right]
            # Leave from the left
            if (left := i - r - 1) >= 0:
                s -= stations[left]
            power[i] = s

        def check(low: int) -> bool:
            diff = [0] * n  # Difference array
            sum_d = built = 0
            for i, p in enumerate(power):
                sum_d += diff[i]  # Accumulate difference values
                m = low - (p + sum_d)
                if m <= 0:
                    continue
                # Build m additional power stations at i+r
                built += m
                if built > k:  # Does not satisfy the requirement
                    return False
                # Add one to the interval [i, i+2r]
                sum_d += m  # diff[i] will not be visited again, so add directly to sum_d
                if (right := i + r * 2 + 1) < n:
                    diff[right] -= m
            return True

        # Binary search on an open interval
        mn = min(power)
        left, right = mn + k // n, mn + k + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left
