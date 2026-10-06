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
        # Prove by mathematical induction that the final result must be a signed sum of the stones
        # This proof reduces the problem to splitting the stones into two groups with sums $positive$ and $negative$,
        # minimizing their absolute difference $abs(positive - negative)$.

        # @lru_cache(None)
        # def dfs(idx, curr):
        #     if idx == len(stones):
        #         return curr if curr >= 0 else inf
        #     return min(dfs(idx+1, curr+stones[idx]), dfs(idx+1, curr-stones[idx]))
        #
        # return dfs(0, 0)

        # Greedy: find a subset sum as close as possible to sum//2
        s = sum(stones)
        t = s // 2
        sums = {0}

        for stone in stones:
            for cs in list(sums):
                if cs + stone < t:
                    sums.add(cs + stone)
                elif cs + stone == t:
                    return s - 2 * t
        return s - 2 * max(sums)
