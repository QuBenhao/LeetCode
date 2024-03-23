import solution
from typing import *
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.isHappy(test_input)

    def isHappy(self, n: int) -> bool:
        @lru_cache(None)
        def helper(x: int) -> int:
            res = 0
            while x:
                x, y = divmod(x, 10)
                res += y * y
            return res

        fast = slow = n
        while fast > 1:
            fast = helper(helper(fast))
            slow = helper(slow)
            if fast > 1 and fast == slow:
                return False
        return True

        # explored = {n}
        # while n > 1:
        #     nxt = 0
        #     while n:
        #         nxt += (n % 10) ** 2
        #         n //= 10
        #     if nxt in explored:
        #         return False
        #     explored.add(nxt)
        #     n = nxt
        # return True
