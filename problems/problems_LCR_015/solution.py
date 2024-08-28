import solution
from typing import *
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findAnagrams(*test_input)

    def findAnagrams(self, s: str, p: str) -> List[int]:
        counts = Counter(p)
        diff = len(counts)
        ans = []
        for i in range(len(s)):
            counts[s[i]] -= 1
            if counts[s[i]] == 0:
                diff -= 1
            elif counts[s[i]] == -1:
                diff += 1
            if i >= len(p) - 1:
                if diff == 0:
                    ans.append(i - len(p) + 1)
                counts[s[i - len(p) + 1]] += 1
                if counts[s[i - len(p) + 1]] == 0:
                    diff -= 1
                elif counts[s[i - len(p) + 1]] == 1:
                    diff += 1
        return ans
