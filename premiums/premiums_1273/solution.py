import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.deleteTreeNodes(*test_input)

    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
                pass