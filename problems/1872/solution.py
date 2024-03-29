import solution
from functools import lru_cache
from itertools import accumulate


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.stoneGameVIII(list(test_input))

    def stoneGameVIII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # 1. 每次取走最左边的x个石子，把他们的和放回最左边，前缀和presum[x]不变
        # 2. 位置i的最大收益为i右边最大的 presum[j] - dp[j] 的j
        for i in range(1, len(stones)):
            stones[i] += stones[i - 1]

        res = stones[-1]
        for num in stones[-2:0:-1]:
            # 我们取到j，获得presum[j]的分数，对手最多能取dp[j]
            # 或者我们跨过j，获得dp[j]的分数
            res = max(num - res, res)
        return res

        # # 移除并放回，前缀和不变
        # # 每次拿的石子必然包括前面的前缀和
        # @lru_cache(None)
        # def dfs(idx):
        #     if idx >= n - 1:
        #         return presum[n]
        #     # 不选当前坐标，选后面的会是dfs(idx+1),选当前坐标会得到presum[idx+1] - dfs(idx+1)。取两者最大值
        #     return max(dfs(idx + 1), presum[idx + 1] - dfs(idx+1))
        #
        # n = len(stones)
        # presum = [0] + list(accumulate(stones))
        # dfs.cache_clear()
        # # 0必须拿
        # return dfs(1)
