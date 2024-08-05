import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findAnagrams(*test_input)

    def findAnagrams(self, s: str, p: str) -> List[int]:
        def maintain(key: int, val: int) -> int:
            before = target[key] == 0
            target[key] += val
            if before:
                return 1
            elif not target[key]:
                return -1
            return 0

        m, n = len(s), len(p)
        ans = []
        if m < n:
            return ans
        target = [0] * 26
        for c in p:
            target[ord(c) - ord('a')] -= 1
        diff = sum(1 for x in target if x)
        for i in range(m):
            diff += maintain(ord(s[i]) - ord('a'), 1)
            if i >= n - 1:
                if diff == 0:
                    ans.append(i - n + 1)
                diff += maintain(ord(s[i - n + 1]) - ord('a'), -1)
        return ans
