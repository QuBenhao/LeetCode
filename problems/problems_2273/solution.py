import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.removeAnagrams(test_input)

    def removeAnagrams(self, words: List[str]) -> List[str]:
        last = None
        ans = []
        for w in words:
            st = "".join(sorted(w))
            if st == last:
                continue
            last = st
            ans.append(w)
        return ans
