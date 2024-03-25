import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.dietPlanPerformance(*test_input)

    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
                pass