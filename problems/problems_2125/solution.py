import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfBeams(test_input)

    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = 0
        for row in bank:
            count = row.count('1')
            ans += count * prev
            if count:
                prev = count
        return ans
