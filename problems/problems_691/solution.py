from collections import Counter, deque
from typing import *

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minStickers(*test_input)

    def minStickers(self, stickers: List[str], target: str) -> int:
        def trans(s):
            cnts = Counter()
            for c in s:
                if c in target:
                    cnts[c] += 1
            return cnts

        available = [c for st in stickers if (c:=trans(st))]
        queue = deque([(target, 0)])
        explored = {target}
        while queue:
            cur, step = queue.popleft()
            if not cur:
                return step
            for avl in available:
                if cur[0] in avl:
                    nxt = cur
                    for k, v in avl.items():
                        nxt = nxt.replace(k, '', v)
                    if nxt not in explored:
                        explored.add(nxt)
                        queue.append((nxt, step + 1))
        return -1
