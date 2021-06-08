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
