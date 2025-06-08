from functools import cache

from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumProfit(*test_input)

    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        dp = [[[-inf] * 3 for _ in range(k + 1)] for _ in range(n + 1)]
        dp[0][0][0] = 0
        for i in range(n):
            for j in range(min(i+2,k+1)):
                for t in range(3):
                    dp[i+1][j][t] = max(dp[i+1][j][t], dp[i][j][t]) # 延续上次结果
                if j > 0: # 从上一次完成一次交易得到当前j次交易后的最大值
                    dp[i+1][j][0] = max(dp[i+1][j][0], dp[i][j-1][1] + prices[i], dp[i][j-1][2] - prices[i])
                dp[i+1][j][1] = max(dp[i+1][j][1], dp[i][j][0] - prices[i]) # 买入
                dp[i+1][j][2] = max(dp[i+1][j][2], dp[i][j][0] + prices[i]) # 卖出
        return max(dp[n][j][0] for j in range(k + 1)) # 不一定要完成k次交易，找到最大值即可
