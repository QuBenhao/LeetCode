import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.generateTag(test_input)

    def generateTag(self, caption: str) -> str:
        words = [s for s in caption.split(" ") if s]
        ans = []
        for i, w in enumerate(words):
            if i == 0:
                ans.append(w.lower())
            else:
                ans.append(w.capitalize())
        return ("#"+"".join(ans))[:100]
