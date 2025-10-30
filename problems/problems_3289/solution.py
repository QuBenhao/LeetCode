from functools import reduce

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getSneakyNumbers(test_input)

    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums) - 2
        y = reduce(lambda x, y: x ^ y, nums)
        match (n - 1) % 4:
            case 0:
                y ^= n - 1
            case 1:
                y ^= 1
            case 2:
                y ^= n
        lb = y & -y
        x1 = x2 = 0
        for i, x in enumerate(nums):
            if i < n:
                if i & lb:
                    x1 ^= i
                else:
                    x2 ^= i
            if x & lb:
                x1 ^= x
            else:
                x2 ^= x
        return [x2, x1]
