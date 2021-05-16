import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canCross(list(test_input))

    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        # @lru_cache(None)
        # def bfs(idx, k):
        #     if k == 0:
        #         return False
        #     if idx == n - 1:
        #         return True
        #     for i in range(idx + 1, n):
        #         diff = stones[i] - stones[idx]
        #         if k - 1 <= diff <= k + 1 and bfs(i, diff):
        #             return True
        #         elif diff > k + 1:
        #             break
        #     return False
        #
        # n = len(stones)
        # if stones[1] != 1:
        #     return False
        # return bfs(1, 1)

        # 动态规划
        # n = len(stones)
        # dp = [[False] * n for _ in range(n)]
        # dp[0][0] = True
        # for i in range(1, n):
        #     for j in range(i - 1, -1, -1):
        #         diff = stones[i] - stones[j]
        #         if diff > j + 1:
        #             break
        #         for d in diff-1,diff,diff+1:
        #             if dp[j][d]:
        #                 dp[i][diff] = True
        #                 break
        #         if i == n - 1 and dp[i][diff]:
        #             return True
        # return False

        @lru_cache(None)
        def dfs(pos, step):
            if pos == stones[-1]:
                return True
            for nxt in -1, 0, 1:
                nxstep = step + nxt
                nxpos = nxstep + pos
                if nxstep > 0 and nxpos in set_stones:
                    if dfs(nxpos, nxstep):
                        return True
            return False

        set_stones = set(stones)
        return dfs(0, 0)
