import solution
from functools import lru_cache
from math import inf
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.lastStoneWeightII(list(test_input))

    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # 数学归纳法 证明 最终结果必然在某种正负取石子中
        # 根据这个证明，原题可以理解为:将原来的石子分成两堆$positive$和$negative$的和，
        # 并使得他们和的差值的绝对值$abs(positive - negative)$尽可能的小。

        # @lru_cache(None)
        # def dfs(idx, curr):
        #     if idx == len(stones):
        #         return curr if curr >= 0 else inf
        #     return min(dfs(idx+1, curr+stones[idx]), dfs(idx+1, curr-stones[idx]))
        #
        # return dfs(0, 0)

        # 贪心: 最接近 sum//2 的组合和
        n = len(stones)
        s = sum(stones)
        t = s // 2
        dp = defaultdict(bool)
        dp[0] = True
        for num in stones:
            for key in sorted(dp.keys(), reverse=True):
                if num + key < t:
                    dp[num + key] = True
                elif num + key == t:
                    return s - 2 * t
        return s - 2 * max(dp.keys())
