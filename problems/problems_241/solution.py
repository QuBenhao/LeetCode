from functools import cache
from itertools import product

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.diffWaysToCompute(test_input)

    def diffWaysToCompute(self, expression: str) -> List[int]:
        @cache
        def dfs(l, r):
            if r < l:
                return [0]
            if all(c.isdigit() for c in expression[l:r + 1]):
                return [int(expression[l:r + 1])]
            res = []
            for i in range(l, r + 1):
                if not expression[i].isdigit():
                    left = dfs(l, i - 1)
                    right = dfs(i + 1, r)
                    for lv, rv in product(left, right):
                        match expression[i]:
                            case '+':
                                res.append(lv + rv)
                            case '-':
                                res.append(lv - rv)
                            case '*':
                                res.append(lv * rv)
            return res

        return dfs(0, len(expression) - 1)
