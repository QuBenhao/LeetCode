from collections import deque
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumCost(*test_input)

    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        trans = [[inf] * 26 for _ in range(26)]
        for i in range(26):
            trans[i][i] = 0
        q = deque()
        for o, c, ct in zip(original, changed, cost):
            a, b = ord(o) - ord('a'), ord(c) - ord('a')
            if ct < trans[a][b]:
                trans[a][b] = ct
                q.append((a, b))
        while q:
            a, b = q.popleft()
            for other in range(26):
                if trans[other][a] + trans[a][b] < trans[other][b]:
                    trans[other][b] = trans[other][a] + trans[a][b]
                    q.append((other, b))

        ans = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            a, b = ord(s) - ord('a'), ord(t) - ord('a')
            if trans[a][b] == inf:
                return -1
            ans += trans[a][b]
        return ans
