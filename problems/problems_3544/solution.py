from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.subtreeInversionSum(*test_input)

    def subtreeInversionSum(self, edges: List[List[int]], nums: List[int], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        n = len(nums)
        memo = [None] * n * k * 2

        def dfs(i, d, c, pa):
            idx = max(c, 0) * n * k + d * n + i
            if memo[idx] is not None:
                return memo[idx]
            # 反转当前或不反转
            ans = nums[i] * c
            if graph[i]:
                ans += sum(dfs(j, max(0, d - 1), c, i) for j in graph[i] if j != pa)
                if d == 0:
                    cur = sum(dfs(j, k - 1, -c, i) for j in graph[i] if j != pa) - nums[i] * c
                    ans = max(ans, cur)
            elif d == 0:
                ans = abs(ans)
            memo[idx] = ans
            return ans

        return dfs(0, 0, 1, -1)
