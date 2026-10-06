import solution
from typing import *
from functools import lru_cache


@lru_cache(None)
def combination_nums(total):
    if total <= 1:
        return 0
    return total * (total - 1) // 2


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.distributeCandies(*test_input)

    def distributeCandies(self, n: int, limit: int) -> int:
        # Total number of ways: C n+2 2
        # Ways for one person to exceed limit: C n+1-limit 2
        # Ways for two people to exceed limit: C n-2*limit 2
        # Ways for three people to exceed limit: C n-1-3*limit 2

        return (combination_nums(n + 2)
                - 3 * combination_nums(n + 1 - limit)
                + 3 * combination_nums(n - 2 * limit)
                - combination_nums(n - 1 - 3 * limit)
                )
