from collections import defaultdict, deque
from functools import cache
from math import inf

from sortedcontainers import SortedSet

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumCost(*test_input)

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        trans = defaultdict(lambda: defaultdict(lambda: inf))
        q = deque()
        for o, c, ct in zip(original, changed, cost):
            q.append((o, c))
            trans[o][c] = min(trans[o][c], ct)
        while q:
            o, c = q.popleft()
            for k, v in trans[c].items():
                if (d := v + trans[o][c]) < trans[o][k]:
                    trans[o][k] = d
                    q.append((o, k))
        lengths = SortedSet()
        for k in trans.keys():
            lengths.add(len(k))

        n = len(source)
        @cache
        def dfs(i):
            if i == n:
                return 0
            if source[i] == target[i]:
                ans = dfs(i + 1)
            else:
                ans = inf
            for l in lengths:
                j = i + l
                if j > n:
                    break
                sps, spt = source[i: j], target[i: j]
                if trans[sps][spt] != inf:
                    ans = min(ans, trans[sps][spt] + dfs(j))

            return ans

        res = dfs(0)
        return res if res != inf else -1
