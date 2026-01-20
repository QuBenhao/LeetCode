from collections import Counter
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.lexSmallestAfterDeletion(test_input)

    def lexSmallestAfterDeletion(self, s: str) -> str:
        counts = Counter(s)
        st = []
        for c in s:
            while st and st[-1] > c and counts[st[-1]] > 1:
                counts[st.pop()] -= 1
            st.append(c)
        while st and counts[st[-1]] > 1:
            counts[st.pop()] -= 1
        return ''.join(st)
