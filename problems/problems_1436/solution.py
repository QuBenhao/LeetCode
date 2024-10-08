import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.destCity(test_input)

    def destCity(self, paths: List[List[str]]) -> str:
        start, end = set(), set()
        for f, t in paths:
            start.add(f)
            end.add(t)
        return (end - start).pop()
