import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sortPermutation(test_input)

    def sortPermutation(self, nums: List[int]) -> int:
        # Every misplaced value must take part in some swap, so k is a
        # submask of all of them; their AND itself works, since that value
        # (or 0) can be swapped with every misplaced value as a buffer.
        ans = -1
        for i, x in enumerate(nums):
            if x != i:
                ans &= x
        return 0 if ans < 0 else ans
