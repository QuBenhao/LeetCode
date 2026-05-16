from collections import deque

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canReach(*test_input)

    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = {start}
        dq = deque([start])
        while dq:
            cur = dq.popleft()
            if arr[cur] == 0:
                return True
            for nxt in (cur + arr[cur], cur - arr[cur]):
                if 0 <= nxt < n and nxt not in visited:
                    visited.add(nxt)
                    dq.append(nxt)
        return False
