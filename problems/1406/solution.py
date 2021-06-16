import solution
from functools import lru_cache
from itertools import accumulate
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.stoneGameIII(list(test_input))

    def stoneGameIII(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: str
        """

        # @lru_cache(None)
        # def dfs(idx):
        #     if idx == n:
        #         return 0
        #     res = -inf
        #     for i in range(idx + 1, min(n + 1, idx + 4)):
        #         res = max(res, presum[i] - presum[idx] - dfs(i))
        #     return res
        #
        # n = len(stoneValue)
        # presum = list(accumulate([0] + stoneValue))
        # ans = dfs(0)
        # if ans > 0:
        #     return "Alice"
        # elif ans == 0:
        #     return "Tie"
        # else:
        #     return "Bob"

        # n = len(stoneValue)
        # presum = list(accumulate([0] + stoneValue))
        # dp = [0] * (n + 3)
        # for i in range(n - 1, -1, -1):
        #     dp[i] = presum[-1] - presum[i] - min(dp[j] for j in range(i + 1, i + 4))
        # ans = dp[0] * 2 - presum[-1]
        # if ans > 0:
        #     return "Alice"
        # elif ans == 0:
        #     return "Tie"
        # else:
        #     return "Bob"

        n = len(stoneValue)
        curr_sum = 0
        # 滚动更新
        dp0 = dp1 = dp2 = 0
        # 倒序递推
        for i in range(n - 1, -1, -1):
            curr_sum += stoneValue[i]
            dp0, dp1, dp2 = curr_sum - min(dp0, dp1, dp2), dp0, dp1
        # Alice的分数减去Bob的分数
        ans = dp0 * 2 - curr_sum
        if ans > 0:
            return "Alice"
        elif ans == 0:
            return "Tie"
        else:
            return "Bob"
