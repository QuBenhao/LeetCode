from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.bestClosingTime(test_input)

    def bestClosingTime(self, customers: str) -> int:
        # For a chosen closing time, add the penalties for preceding Ns and following Ys
        # ys = customers.count('Y')
        # ns = 0
        # ans_t, ans = 0, inf
        # for i, c in enumerate(customers + "N"):
        #     if (cur := ns + ys) < ans:
        #         ans_t, ans = i, cur
        #     if c == 'N':
        #         ns += 1
        #     else:
        #         ys -= 1
        """
        The code above shows that we only care about the minimum value of ns+ys.
        The initial value of ys is fixed, so its exact value is unnecessary.
        """
        ns = 0
        ans_t, ans = 0, inf
        for i, c in enumerate(customers + "N"):
            if ns < ans:
                ans_t, ans = i, ns
            ns += 1 if c == "N" else -1
        return ans_t
