from collections import Counter
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.lexSmallestAfterDeletion(test_input)

    def lexSmallestAfterDeletion(self, s: str) -> str:
        left = Counter(s)
        st = []
        for ch in s:
            while st and ch < st[-1] and left[st[-1]] > 1:
                left[st.pop()] -= 1
            st.append(ch)
        while left[st[-1]] > 1:
            left[st.pop()] -= 1
        return "".join(st)
