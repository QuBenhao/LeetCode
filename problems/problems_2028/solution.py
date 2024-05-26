import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.missingRolls(*test_input)

    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (n + len(rolls)) - sum(rolls)
        if not n <= total <= 6 * n:
            return []
        avg, extra = divmod(total, n)
        return [avg + 1] * extra + [avg] * (n - extra)
