from collections import defaultdict

from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumValueSum(*test_input)

    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(_u, _pa) -> Tuple[int, int]:
            # f0: 以_u为根的子树中, 除去_u, _u和k异或了偶数次的最大值
            # f1: 以_u为根的子树中, 除去_u, _u和k异或了奇数次的最大值
            f0, f1 = 0, -inf
            for _v in graph[_u]:
                if _v == _pa:
                    continue
                r0, r1 = dfs(_v, _u)
                f0, f1 = max(f0 + r0, f1 + r1), max(f0 + r1, f1 + r0)
            return max(f0 + nums[_u], f1 + (nums[_u] ^ k)), max(f0 + (nums[_u] ^ k), f1 + nums[_u])

        return dfs(0, -1)[0]
