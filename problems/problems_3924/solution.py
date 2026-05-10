from collections import defaultdict, deque
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumThreshold(*test_input)

    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        def check(x):
            dq = deque([source])
            heavy = [inf] * n
            heavy[source] = 0
            while dq:
                cur = dq.popleft()
                for nxt, weight in graph[cur]:
                    h = heavy[cur]
                    if weight > x:
                        h += 1
                    if h < heavy[nxt]:
                        heavy[nxt] = h
                        dq.append(nxt)
            return heavy[target] <= k

        if not check(10**9):
            return -1

        l, r = 0, 10**9
        while l < r:
            mid = l + (r - l) // 2
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l
