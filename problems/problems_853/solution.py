import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.carFleet(*test_input)

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        st = []
        for p, s in sorted(zip(position, speed), key=lambda x: x[0]):
            # Avoid precision issues from division
            # A car on the left that would arrive sooner merges with a slower-arriving car on the right, giving a monotonically increasing stack
            while st and st[-1][0] * s <= (target - p) * st[-1][1]:
                st.pop()
            st.append(((target - p), s))
        return len(st)
