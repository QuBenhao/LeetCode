import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.mergeAdjacent(test_input)

    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        st = []
        for num in nums:
            cur = num
            while st and st[-1] == cur:
                st.pop()
                cur <<= 1
            st.append(cur)
        return st
