import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.centeredSubarrays(test_input)

    def centeredSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            st = set()
            sm = 0
            for j in range(i, n):
                st.add(nums[j])
                sm += nums[j]
                if sm in st:
                    ans += 1
        return ans
