import solution
from collections import Counter
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findLucky(test_input)

    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        return max([num for num, count in counter.items() if num == count], default=-1)
