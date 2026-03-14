from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getHappyString(*test_input)

    def getHappyString(self, n: int, k: int) -> str:
        bs = 1 << (n - 1)
        if k > 3 * bs:
            return ""
        # 第一位填a, 后面有2^(n-1)种
        if k > 2 * bs:
            ans = "c"
            k -= 2 * bs
        elif k > bs:
            ans = "b"
            k -= bs
        else:
            ans = "a"
        for i in range(n - 1, 0, -1):
            cur = 1 << (i - 1)
            choices = ['a', 'b', 'c']
            choices.remove(ans[-1])
            if k > cur:
                ans += choices[1]
                k -= cur
            else:
                ans += choices[0]
        return ans
