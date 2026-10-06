import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countQuadruplets(test_input)

    def countQuadruplets(self, nums: List[int]) -> int:
        cnt4 = 0
        cnt3 = [0] * len(nums)
        for l in range(2, len(nums)):
            cnt2 = 0
            for j in range(l):
                if nums[j] < nums[l]:  # 3 < 4
                    cnt4 += cnt3[j]
                    # Treat j as i and l as k; now nums[i] < nums[k], corresponding to 1 < 2
                    cnt2 += 1
                else:  # Treat l as k; now nums[j] > nums[k], corresponding to 3 > 2
                    cnt3[j] += cnt2
        return cnt4
