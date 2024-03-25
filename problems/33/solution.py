import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.search(*test_input)

    def search(self, nums: List[int], target: int) -> int:
            pass