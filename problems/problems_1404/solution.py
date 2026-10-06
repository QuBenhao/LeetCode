import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numSteps(test_input)

    def numSteps(self, s: str) -> int:
        # carry = 0
        # ans = len(s) - 1 # Every bit after the first, whether 1 or 0, requires at least one operation
        # for i in range(len(s) - 1, 0, -1):
        #     cur = carry + int(s[i])
        #     ans += 1 if cur == 1 else 0 # Odd numbers require an extra +1
        #     carry = 0 if cur == 0 else 1 # Generate the carry
        # return ans + carry

        # The pattern above shows that only zeros to the left of the rightmost 1 contribute an extra odd-number operation
        ans = len(s) - 1
        if (idx := s.rfind('1')) > 0:
            # Each zero to the left of the rightmost 1 requires an extra +1, and positions idx and 0 each require +1
            ans += s.count('0', 1, idx) + 2
        return ans
