import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canMakeArithmeticProgression(test_input)

    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        d = arr[1] - arr[0]
        last = arr[1]
        for i in range(2, len(arr)):
            if arr[i] - last != d:
                return False
            last = arr[i]
        return True
