import solution
from typing import *

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxmiumScore(*test_input)

    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort(reverse=True)
        s = sum(cards[:cnt])
        if s % 2 == 0:
            return s

        def replace_sum(x: int) -> int:
            for v in cards[cnt:]:
                if v % 2 != x % 2:
                    return s - x + v
            return 0

        cur = cards[cnt - 1]
        ans = replace_sum(cur)
        for v in cards[cnt-1::-1]:
            if v % 2 != cur % 2:
                ans = max(ans, replace_sum(v))
                break
        return ans
