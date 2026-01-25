import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rotateElements(*test_input)

    def rotateElements(self, nums: List[int], k: int) -> List[int]:
        vals = [num for num in nums if num >= 0]
        if not vals:
            return nums
        k %= len(vals)
        vals = vals[k:] + vals[:k]
        ans = list(nums)
        i = 0
        for j, num in enumerate(ans):
            if num < 0:
                continue
            ans[j] = vals[i]
            i += 1
        return ans
