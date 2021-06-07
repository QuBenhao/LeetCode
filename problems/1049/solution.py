import solution
from functools import lru_cache
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.lastStoneWeightII(list(test_input))

    def lastStoneWeightII(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        # 数学归纳法 证明 最终结果必然在某种正负取石子中
        @lru_cache(None)
        def dfs(idx, curr):
            if idx == len(stones):
                return curr if curr >= 0 else inf
            return min(dfs(idx+1, curr+stones[idx]), dfs(idx+1, curr-stones[idx]))

        return dfs(0, 0)
