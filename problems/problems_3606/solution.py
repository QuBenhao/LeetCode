import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.validateCoupons(*test_input)

    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        categories = ["electronics", "grocery","pharmacy","restaurant"]
        valids = []
        for c, b, i in zip(code, businessLine, isActive):
            if i and b in categories and c and all(ch.isalnum() or ch == '_' for ch in c):
                valids.append((b, c))
        valids.sort(key=lambda x: (categories.index(x[0]), x[1]))
        return [c for _, c in valids]
