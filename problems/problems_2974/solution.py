import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberGame(test_input)

    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        ans = []
        for i in range(len(nums) // 2):
            last = nums.pop()
            ans.append(nums.pop())
            ans.append(last)
        return ans
