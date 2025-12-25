from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.bestClosingTime(test_input)

    def bestClosingTime(self, customers: str) -> int:
        # 选某一个点, 前面的N累加代价, 后面的Y累加代价
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
        从上面的代码中可以看出, 我们在乎的是ns+ys的和的最小值
        ys一开始是多少是固定的, 具体值其实不需要知道
        """
        ns = 0
        ans_t, ans = 0, inf
        for i, c in enumerate(customers + "N"):
            if ns < ans:
                ans_t, ans = i, ns
            ns += 1 if c == "N" else -1
        return ans_t
