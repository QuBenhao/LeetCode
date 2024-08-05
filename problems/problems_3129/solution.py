import solution
from typing import *
from functools import cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfStableArrays(*test_input)

    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        mod = 10 ** 9 + 7

        @cache
        def dfs(z, o, cur):
            """
            :param z: the number of zeros
            :param o: the number of ones
            :param cur: the current number
            """
            if not z:
                # we should fill one from now on, and it should be less than or equal to limit
                return 1 if cur == 1 and o <= limit else 0
            if not o:
                # we should fill one zero now on, and it should be less than or equal to limit
                return 1 if cur == 0 and z <= limit else 0
            if cur == 0:
                # 容斥原理
                # we can fill zero or one, but when we fill too many zeros, we should minus exceed limit zeros case
                return (dfs(z - 1, o, 0) + dfs(z - 1, o, 1) - (dfs(z - limit - 1, o, 1) if z > limit else 0)) % mod
            # we can fill zero or one, but when we fill too many ones, we should minus exceed limit ones case
            return (dfs(z, o - 1, 0) + dfs(z, o - 1, 1) - (dfs(z, o - limit - 1, 0) if o > limit else 0)) % mod

        res = (dfs(zero, one, 0) + dfs(zero, one, 1)) % mod
        dfs.cache_clear()
        return res
