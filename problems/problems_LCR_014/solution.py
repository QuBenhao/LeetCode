import solution
from typing import *
from collections import Counter

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkInclusion(*test_input)

    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = Counter(s1)
        c2 = Counter()
        for i in range(len(s2)):
            c2[s2[i]] += 1
            if i >= len(s1) - 1:
                if all(c1[key] == c2[key] for key in c1.keys()):
                    return True
                c2[s2[i - len(s1) + 1]] -= 1
        return False
