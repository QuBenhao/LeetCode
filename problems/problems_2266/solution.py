from functools import cache

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countTexts(test_input)

    def countTexts(self, pressedKeys: str) -> int:
        mod = 10 ** 9 + 7
        possibilities = {'2': 3, '3': 3, '4': 3, '5': 3, '6': 3, '7': 4, '8': 3, '9': 4}
        n = len(pressedKeys)

        @cache
        def dfs(i: int) -> int:
            if i == n:
                return 1
            cur = possibilities[pressedKeys[i]]
            ans = 0
            for nxt in range(i, min(i + cur, n)):
                if pressedKeys[nxt] != pressedKeys[i]:
                    break
                ans = (ans + dfs(nxt + 1)) % mod
            return ans

        return dfs( 0)
