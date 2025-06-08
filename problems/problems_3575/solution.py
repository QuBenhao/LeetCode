from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.goodSubtreeSum(*test_input)

    def goodSubtreeSum(self, vals: List[int], par: List[int]) -> int:
        n = len(vals)
        graph = defaultdict(list)
        root = -1
        for i, p in enumerate(par):
            if p == -1:
                root = i
            else:
                graph[p].append(i)

        def get_mask(u):
            mask = 0
            for d in map(int, str(vals[u])):
                if (mask >> d) & 1:
                    return -1
                mask |= 1 << d
            return mask

        max_scores = [0] * n

        def dfs(u: int) -> dict[int, int]:
            mask = get_mask(u)
            dp = {0: 0} if mask == -1 else {mask: vals[u]}
            for v in graph[u]:
                child_dp = dfs(v)
                new_dp = dp.copy()
                for m1, s1 in dp.items():
                    for m2, s2 in child_dp.items():
                        if (m1 & m2) == 0:
                            new_mask = m1 | m2
                            if new_mask not in new_dp or new_dp[new_mask] < s1 + s2:
                                new_dp[new_mask] = s1 + s2
                for m2, s2 in child_dp.items():
                    if m2 not in new_dp or new_dp[m2] < s2:
                        new_dp[m2] = s2
                dp = new_dp
            max_scores[u] = max(dp.values())
            return dp

        dfs(root)
        ans = 0
        MOD = 10**9 + 7
        for s in max_scores:
            ans = (ans + s) % MOD
        return ans
