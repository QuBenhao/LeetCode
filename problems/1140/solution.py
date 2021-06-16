import solution
from functools import lru_cache
from itertools import accumulate


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.stoneGameII(list(test_input))

    def stoneGameII(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        @lru_cache(None)
        def dfs(idx, curr):
            if idx == n:
                return 0
            # 剩余的全部石子可以被一个人拿走了
            if n - idx <= 2 * curr:
                return presum[-1] - presum[idx]
            # 当前能拿到的最大值为 总共剩余的石子减去让对方拿到的尽可能小
            return presum[-1] - presum[idx] - min(dfs(idx + i, max(i, curr)) for i in range(1, 2 * curr + 1))

        n = len(piles)
        presum = list(accumulate([0] + piles))
        return dfs(0, 1)
