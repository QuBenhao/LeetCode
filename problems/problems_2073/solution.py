import solution
from typing import *
from collections import deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.timeRequiredToBuy(*test_input)

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        q = deque([i for i in range(n)])
        ans = 0
        while tickets[k]:
            cur = q.popleft()
            tickets[cur] -= 1
            if tickets[cur] > 0:
                q.append(cur)
            ans += 1
        return ans
