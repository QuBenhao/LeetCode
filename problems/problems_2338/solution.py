from collections import defaultdict, deque
from math import sqrt, comb

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.idealArrays(*test_input)

    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10 ** 9 + 7
        g = defaultdict(list)
        deg = [0 for _ in range(maxValue + 1)]
        for i in range(1, maxValue + 1):
            if i != 1:
                g[i].append(1)
                deg[1] += 1
            for j in range(2, int(sqrt(i)) + 1):
                if i % j == 0:
                    g[i].append(j)
                    deg[j] += 1
                    if i // j != j:
                        g[i].append(i // j)
                        deg[i // j] += 1

        ans = 0
        # 只考虑相邻点不同(拓扑序)
        # dp[i]表示以i开头的最长序列总数
        dp = [[0 for _ in range(21)] for _ in range(maxValue + 1)]
        queue = deque()
        for i in range(1, maxValue + 1):
            if deg[i] == 0:
                queue.append(i)
            dp[i][1] = 1

        while queue:
            cur = queue.popleft()
            for nxt in g[cur]:
                for i in range(20):
                    dp[nxt][i + 1] += dp[cur][i]
                deg[nxt] -= 1
                if deg[nxt] == 0:
                    queue.append(nxt)

        def cal(v):
            nonlocal n, mod
            ans = 0
            for i in range(1, min(n + 1, 21)):
                ans += comb(n - 1, i - 1) % mod * v[i]
                ans %= mod
            return ans

        for i in range(1, maxValue + 1):
            ans += cal(dp[i])
            ans %= mod

        return ans

