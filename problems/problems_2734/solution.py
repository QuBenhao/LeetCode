import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallestString(test_input)

    def smallestString(self, s: str) -> str:
        left = 0
        while left < len(s) and s[left] == 'a':
            left += 1
        if left == len(s):
            return s[:len(s) - 1] + 'z'
        right = left
        ans = s[:left]
        while right < len(s) and s[right] != 'a':
            ans += chr(ord(s[right]) - 1)
            right += 1
        return ans + s[right:]
