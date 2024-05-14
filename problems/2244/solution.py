import solution
from typing import *
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumRounds(test_input)

    def minimumRounds(self, tasks: List[int]) -> int:
        cnts = Counter(tasks)
        ans = 0
        for cnt in cnts.values():
            if cnt == 1:
                return -1
            match cnt % 3:
                case 1:
                    ans += (cnt - 4) // 3 + 2
                case 2:
                    ans += cnt // 3 + 1
                case _:
                    ans += cnt // 3
        return ans
