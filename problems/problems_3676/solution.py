import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.bowlSubarrays(test_input)

    def bowlSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        left_greater = [-1] * n
        right_greater = [-1] * n
        st = []
        for i in range(n):
            while st and nums[st[-1]] < nums[i]:
                right_greater[st.pop()] = i
            if st:
                left_greater[i] = nums[st[-1]]
            st.append(i)
        ans = 0
        for l, r in zip(left_greater, right_greater):
            if l != -1 and r != -1:
                ans += 1
        return ans
