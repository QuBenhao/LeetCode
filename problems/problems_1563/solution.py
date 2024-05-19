import solution
from functools import lru_cache
from itertools import accumulate
import bisect


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.stoneGameV(list(test_input))

    def stoneGameV(self, stoneValue):
        """
        :type stoneValue: List[int]
        :rtype: int
        """

        @lru_cache(None)
        def dfs(i, j):
            if i >= j:
                return 0
            ans = 0
            half = (presum[j + 1] + presum[i]) / 2
            # 使用二分查找左右的大小中心位置
            idx = bisect.bisect_left(presum, half, lo=i, hi=j + 1)
            # idx 左边, left更小; idx 右边, right更小
            if presum[idx] == half:
                ans = max(ans, left_dfs(i, idx), right_dfs(idx, j))
            else:
                ans = max(ans, left_dfs(i, idx - 1))
                ans = max(ans, right_dfs(idx, j))
            return ans

        @lru_cache(None)
        def left_dfs(i, j):
            if i >= j:
                return 0
            return max(presum[j] - presum[i] + dfs(i, j - 1), left_dfs(i, j - 1))

        @lru_cache(None)
        def right_dfs(i, j):
            if i >= j + 1:
                return 0
            return max(presum[j + 1] - presum[i] + dfs(i, j), right_dfs(i + 1, j))

        presum = [0] + list(accumulate(stoneValue))
        return dfs(0, len(stoneValue) - 1)
