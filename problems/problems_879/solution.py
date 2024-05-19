import solution
from functools import lru_cache
from math import inf
from itertools import accumulate
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.profitableSchemes(*test_input)

    def profitableSchemes(self, n, minProfit, group, profit):
        """
        :type n: int
        :type minProfit: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        # @lru_cache(None)
        # def dfs(idx, p, pro):
        #     if idx == len(group):
        #         return int(pro == minProfit)
        #     if 0 <= p < group[idx]:
        #         return dfs(idx+1,p,pro)
        #     if p >= presum_g[-1] - presum_g[idx]:
        #         p = inf
        #     return dfs(idx+1,p-group[idx],min(minProfit, pro+profit[idx]))+dfs(idx+1,p,pro)
        #
        # presum_g = list(accumulate([0] + group))
        #
        # return dfs(0,n,0) % (10**9+7)

        # dp = Counter()
        # dp[(0,0)] = 1
        # for g,p in zip(group, profit):
        #     for tg, tp in sorted(dp.keys(),reverse=True):
        #         if tg + g <= n:
        #             dp[(tg+g, min(minProfit, tp+p))] += dp[(tg,tp)]
        # return sum(val for (_,v),val in dp.items() if v == minProfit) % (10 ** 9 + 7)

        mod = 10 ** 9 + 7
        # 容斥原理 g <= n, p >= minProfit的组合个数为 g<=n的个数减去g<=n,p < minProfit的个数
        # 先求 g<=n 的组合数
        dp1 = [0] * (n + 1)
        dp1[0] = 1
        for g in group:
            for i in range(n, g - 1, -1):
                dp1[i] += dp1[i - g]
        # p < minProfit的组合数为0
        if not minProfit:
            return sum(dp1) % mod

        # 求 g <= n, p < minProfit的组合数
        dp2 = [[0] * minProfit for _ in range(n + 1)]
        dp2[0][0] = 1
        for g, p in zip(group, profit):
            for i in range(n, g - 1, -1):
                for j in range(minProfit - 1, p - 1, -1):
                    dp2[i][j] += dp2[i - g][j - p]
        return (sum(dp1) - sum(sum(dp2[i]) for i in range(n + 1))) % mod
