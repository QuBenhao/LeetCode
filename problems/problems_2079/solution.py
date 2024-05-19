import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.wateringPlants(*test_input)

    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = len(plants)
        water = capacity
        for i, need in enumerate(plants):
            if water < need:
                ans += i * 2
                water = capacity
            water -= need
        return ans
