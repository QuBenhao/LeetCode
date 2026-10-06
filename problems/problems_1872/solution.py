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
        # 1. Remove the leftmost x stones and put their sum on the left; presum[x] remains unchanged
        # 2. The maximum gain at i is the largest presum[j] - dp[j] over j to its right
        for i in range(1, len(stones)):
            stones[i] += stones[i - 1]

        res = stones[-1]
        for num in stones[-2:0:-1]:
            # Stop at j to gain presum[j], while the opponent can gain at most dp[j]
            # Or skip j and retain the score dp[j]
            res = max(num - res, res)
        return res

        # # Removing and replacing leaves prefix sums unchanged
        # # Each move includes the preceding prefix sum
        # @lru_cache(None)
        # def dfs(idx):
        #     if idx >= n - 1:
        #         return presum[n]
        #     # Skipping this index gives dfs(idx+1); choosing it gives presum[idx+1] - dfs(idx+1). Take the maximum
        #     return max(dfs(idx + 1), presum[idx + 1] - dfs(idx+1))
        #
        # n = len(stones)
        # presum = [0] + list(accumulate(stones))
        # dfs.cache_clear()
        # # Position 0 must be taken
        # return dfs(1)
