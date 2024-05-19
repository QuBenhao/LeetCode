import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minAvailableDuration(*test_input)

    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
                pass