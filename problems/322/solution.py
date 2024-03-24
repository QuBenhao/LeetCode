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
        二进制转换，$a+b+c=x$求解可以转化为$2^a*2^b*2^c=2^x$，也就是$1 << x = 1 << a << b << c$
        题目可以转化为：
            我们的取硬币操作可以理解为右移操作，
            取的总数变为$1<<amount$，
            我们最少需要右移多少次直到最小位出现1，
            也就是我们找到了取$1<<0$的路径了。这个时候其他位是不是1不影响，只要有一个路径出现就代表找到了。
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
