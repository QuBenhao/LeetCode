import solution
from collections import Counter
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isPossibleToSplit(test_input)

    def isPossibleToSplit(self, nums: List[int]) -> bool:
        return all(x < 3 for x in counter.values()) if (counter := Counter(nums)) else False
