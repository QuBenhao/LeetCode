import solution
from typing import *
from math import inf

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxDistance(test_input)

    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val, max_val = inf, -inf
        ans = 0
        for arr in arrays:
            ans = max(ans, max(arr) - min_val, max_val - min(arr))
            min_val = min(min_val, arr[0])
            max_val = max(max_val, arr[-1])
        return ans
