import math

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.replaceNonCoprimes(test_input)

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        st = []
        for num in nums:
            while st and (g := math.gcd(st[-1], num)) != 1:
                num = st.pop() * num // g
            st.append(num)
        return st
