import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumEnergy(*test_input)

    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        for i in range(n - k - 1, -1, -1):
            energy[i] += energy[i + k]
        return max(energy)
