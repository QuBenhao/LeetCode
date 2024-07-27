import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getSmallestString(*test_input)

    def getSmallestString(self, s: str, k: int) -> str:
        def distance(a, b):
            return min((ord(b) - ord(a) + 26) % 26, (ord(a) - ord(b) + 26) % 26)

        ans = []
        idx = 0
        while idx < len(s) and k:
            if s[idx] != 'a':
                d = distance(s[idx], 'a')
                if d <= k:
                    k -= d
                    ans.append('a')
                else:
                    ans.append(chr(ord(s[idx]) - k))
                    k = 0
            else:
                ans.append(s[idx])
            idx += 1
        ans.append(s[idx:])
        return ''.join(ans)
