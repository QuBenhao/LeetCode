import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findMinimumTime(test_input)

    def findMinimumTime(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda t: t[1])
        # The stack stores inclusive interval endpoints and the cumulative interval length from the bottom through each entry
        st = [(-2, -2, 0)]  # Sentinel that does not overlap any interval
        for start, end, d in tasks:
            _, r, s = st[bisect_left(st, (start,)) - 1]
            d -= st[-1][2] - s  # Subtract time points when the computer is already running
            if start <= r:  # start lies inside st[i]
                d -= r - start + 1  # Subtract time points when the computer is already running
            if d <= 0:
                continue
            while end - st[-1][1] <= d:  # Fill the interval's suffix with the remaining d time points
                l, r, _ = st.pop()
                d += r - l + 1  # Merge intervals
            st.append((end - d + 1, end, st[-1][2] + d))
        return st[-1][2]
