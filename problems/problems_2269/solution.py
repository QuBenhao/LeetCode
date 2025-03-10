import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.divisorSubstrings(*test_input)

    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)
        cur = 0
        ans = 0
        for i in range(k):
            cur = cur * 10 + int(num_str[i])
        if cur and num % cur == 0:
            ans += 1
        for i in range(k, len(num_str)):
            cur = cur * 10 + int(num_str[i]) - int(num_str[i - k]) * 10 ** k
            if cur and num % cur == 0:
                ans += 1
        return ans
