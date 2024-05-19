import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.insert(*test_input)

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            pass