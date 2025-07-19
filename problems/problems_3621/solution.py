from functools import lru_cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.popcountDepth(*test_input)

    def popcountDepth(self, n: int, k: int) -> int:
        if k == 0:
            return 1

        length = n.bit_length()
        possible_nums = set()
        for i in range(2, length + 1):
            if DEPTH[i] + 1 == k:
                possible_nums.add(i)
        if k == 1:
            possible_nums.add(1)

        if not possible_nums:
            return 0

        @lru_cache(None)
        def dfs(pos, limit, nums):
            if length - pos < nums or nums < 0:
                return 0
            if pos == length:
                return 1
            ans = 0
            nd = (n >> (length - pos - 1)) & 1
            l = 1 if not limit else nd
            for d in range(l + 1):
                ans += dfs(pos + 1, limit and d == nd, nums - d)
            return ans

        res = 0
        for p in possible_nums:
            res += dfs(0, True, p)
            if p == 1:
                res -= 1
        return res


MAX_N = (10 ** 15).bit_length()
DEPTH = [0] * (MAX_N + 1)
DEPTH[1] = 1
for _i in range(2, MAX_N + 1):
    _j = _i
    while _j > 1:
        DEPTH[_i] += 1
        _j = bin(_j).count('1')
