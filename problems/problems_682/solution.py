import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.calPoints(test_input)

    def calPoints(self, operations: List[str]) -> int:
        ans, cur = 0, []
        for op in operations:
            match op:
                case "+":
                    cur.append(cur[-1] + cur[-2])
                    ans += cur[-1]
                case "D":
                    cur.append(cur[-1] * 2)
                    ans += cur[-1]
                case "C":
                    ans -= cur.pop()
                case _:
                    cur.append(int(op))
                    ans += cur[-1]
        return ans
