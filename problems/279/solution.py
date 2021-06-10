import solution
from functools import lru_cache
from math import inf,sqrt


class Solution(solution.Solution):
    ans = inf

    def solve(self, test_input=None):
        return self.numSquares(test_input)

    def numSquares(self, n: int) -> int:
        return self.answer(n, 0)

    @lru_cache(None)
    def answer(self, n, ans):
        if ans >= self.ans:
            return inf
        if n == 0:
            self.ans = ans
            return ans
        rg = int(sqrt(n))
        res = inf
        for i in range(rg, rg // 2, -1):
            res = min(res, self.answer(n - i * i, ans + 1))
        return res
