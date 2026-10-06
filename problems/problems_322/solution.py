import solution
from typing import *
from functools import lru_cache
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.coinChange(*test_input)

    def coinChange(self, coins: List[int], amount: int) -> int:
        # @lru_cache(None)
        # def dfs(remain):
        #     return min(dfs(remain - c) for c in coins) + 1 if remain > 0 else (0 if not remain else inf)
        #
        # return -1 if (ans := dfs(amount)) == inf else ans

        """
        Binary transformation: solving $a+b+c=x$ can be transformed into $2^a*2^b*2^c=2^x$, or $1 << x = 1 << a << b << c$.
        The problem can be reframed as follows:
            Taking a coin is a right-shift operation.
            Represent the total as $1<<amount$.
            Find the fewest right shifts needed for a 1 to appear in the lowest bit.
            This means a path to $1<<0$ has been found. Whether other bits are 1 does not matter; one such path is enough.
        """
        if not amount:
            return 0
        step, dp = 0, 1 << amount
        while dp:
            nxt = 0
            step += 1
            for c in coins:
                nxt |= dp >> c
            if nxt & 1:
                return step
            dp = nxt
        return -1
