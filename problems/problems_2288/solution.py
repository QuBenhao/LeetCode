import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.discountPrices(*test_input)

    def discountPrices(self, sentence: str, discount: int) -> str:
        ans = []
        for s in sentence.split(" "):
            if s.startswith("$") and len(s) > 1 and all(s[i].isdigit() for i in range(1, len(s))):
                ans.append("$%.2f" % (int(s[1:]) * (100 - discount) / 100))
            else:
                ans.append(s)
        return " ".join(ans)
