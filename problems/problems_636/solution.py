import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.exclusiveTime(*test_input)

    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        def helper(log):
            idx, mark, time = log.split(":")
            return int(idx), mark == "start", int(time)

        stack, ans, total = [], [0] * n, 0
        for lg in logs:
            idx, is_start, time = helper(lg)
            if is_start:
                stack.append(total - time)
            else:
                d = stack.pop()
                diff = time + 1 + d - total
                ans[idx] += diff
                total += diff
        return ans
