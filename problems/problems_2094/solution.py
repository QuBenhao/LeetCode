import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findEvenNumbers(test_input)

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        cnt = [0] * 10
        for dg in digits:
            cnt[dg] += 1
        ans = []

        def dfs(i, num):
            if i == 3:
                ans.append(num)
                return
            for d, c in enumerate(cnt):
                if c == 0 or (i == 2 and d % 2 != 0) or (i == 0 and d == 0):
                    continue
                cnt[d] -= 1
                dfs(i + 1, num * 10 + d)
                cnt[d] += 1

        dfs(0, 0)
        return ans
