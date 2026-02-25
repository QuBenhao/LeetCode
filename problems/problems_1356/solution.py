import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.sortByBits(test_input)

    def sortByBits(self, arr: List[int]) -> List[int]:
        return list(sorted(arr, key=lambda x: (x.bit_count(), x)))
