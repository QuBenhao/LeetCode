import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumAND(*test_input)

    def maximumAND(self, nums: List[int], k: int, m: int) -> int:
        def check(x):
            vals = []
            for num in nums:
                diff = x & ~num
                if diff == 0:
                    vals.append(0)
                    continue
                h = diff.bit_length() - 1
                mask = (1 << (h + 1)) - 1
                vals.append((x & mask) - (num & mask))
            vals.sort()
            return sum(vals[:m])

        ans = 0
        for i in range(30, -1, -1):
            t = ans | 1 << i
            if check(t) <= k:
                ans |= t
        return ans
