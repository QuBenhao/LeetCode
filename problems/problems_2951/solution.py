import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findPeaks(test_input)

    def findPeaks(self, mountain: List[int]) -> List[int]:
        return [i for i in range(1, len(mountain) - 1) if
                mountain[i - 1] < mountain[i] and mountain[i] > mountain[i + 1]]
