import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        houses, cost, m, n, target = test_input
        return self.minCost(houses, cost, m, n, target)

    def minCost(self, houses, cost, m, n, target):
        """
        :type houses: List[int]
        :type cost: List[List[int]]
        :type m: int
        :type n: int
        :type target: int
        :rtype: int
        """

        @lru_cache(None)
        def dfs(idx, color, t):
            if t < 0 or t > m - idx:
                return float("inf")
            if idx == m:
                return 0
            curr = float("inf")
            if houses[idx]:
                if houses[idx] != color:
                    curr = min(curr, dfs(idx + 1, houses[idx], t - 1))
                else:
                    curr = min(curr, dfs(idx + 1, houses[idx], t))
            else:
                for i in range(1, n + 1):
                    houses[idx] = i
                    if i != color:
                        curr = min(curr, dfs(idx + 1, houses[idx], t - 1) + cost[idx][i - 1])
                    else:
                        curr = min(curr, dfs(idx + 1, houses[idx], t) + cost[idx][i - 1])
                houses[idx] = 0
            return curr

        res = dfs(0, 0, target)
        if res == float("inf"):
            return -1
        return res

        # # house, color, target
        # # dp[i][j][t] = min(dp[i-1][j][t], min(dp[i][j'][t-1]))  (j' != j)
        # dp = [[[float("inf")] * target for _ in range(n)] for _ in range(m)]
        # # 初始将一个房子染色的情况更新
        # if houses[0]:
        #     dp[0][houses[0] - 1][0] = 0
        # else:
        #     for j in range(n):
        #         dp[0][j][0] = cost[0][j]
        # for i in range(1,m):
        #     if houses[i]:
        #         color = houses[i] - 1
        #         for t in range(target):
        #             dp[i][color][t] = dp[i-1][color][t]
        #             if t:
        #                 for j in range(n):
        #                     if j != color:
        #                         dp[i][color][t] = min(dp[i][color][t], dp[i-1][j][t-1])
        #     else:
        #         for j in range(n):
        #             for t in range(target):
        #                 dp[i][j][t] = dp[i-1][j][t]
        #                 if t:
        #                     for j_ in range(n):
        #                         if j_ != j:
        #                             dp[i][j][t] = min(dp[i][j][t], dp[i-1][j_][t-1])
        #                 dp[i][j][t] += cost[i][j]
        # ans = float("inf")
        # if houses[-1]:
        #     ans = dp[-1][houses[-1]-1][target-1]
        # else:
        #     for j in range(n):
        #         ans = min(ans, dp[-1][j][target-1])
        # return ans if ans != float("inf") else -1
