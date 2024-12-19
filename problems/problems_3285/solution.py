import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.stableMountains(*test_input)

    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [i for i in range(1, len(height)) if height[i - 1] > threshold]
