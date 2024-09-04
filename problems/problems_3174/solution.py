import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.clearDigits(test_input)

    def clearDigits(self, s: str) -> str:
        st = []
        for c in s:
            if c.isdigit():
                if st:
                    st.pop()
            else:
                st.append(c)
        return "".join(st)
