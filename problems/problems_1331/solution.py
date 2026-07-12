import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.arrayRankTransform(test_input)

    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {v: i for i, v in enumerate(sorted(set(arr)), 1)}
        return [rank[v] for v in arr]
