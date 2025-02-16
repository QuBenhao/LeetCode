import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.replaceElements(test_input)

    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], right_max = right_max, max(right_max, arr[i])
        return arr
