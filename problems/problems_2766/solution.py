import solution
from typing import *
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.relocateMarbles(*test_input)

    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        s = set(nums)
        for f, t in zip(moveFrom, moveTo):
            s.remove(f)
            s.add(t)
        return sorted(s)
