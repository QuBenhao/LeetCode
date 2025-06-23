from itertools import product

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.ambiguousCoordinates(test_input)

    def ambiguousCoordinates(self, s: str) -> List[str]:
        def is_valid(num: str) -> bool:
            return len(num) > 0 and (len(num) == 1 or num[0] != '0' or num[-1] != '0')

        def add_point(num: str) -> List[str]:
            if len(num) == 1 or num[-1] == '0':
                return [num]
            if num[0] == '0':
                return [num[0] + '.' + num[1:]]
            res = [num[:i] + '.' + num[i:] for i in range(1, len(num))]
            res.append(num)
            return res

        s = s[1:-1]  # Remove the parentheses
        ans = []
        for idx in range(1, len(s)):
            left = s[:idx]
            right = s[idx:]
            if not is_valid(left) or not is_valid(right):
                continue
            possible_left = add_point(left)
            possible_right = add_point(right)
            for l, r in product(possible_left, possible_right):
                ans.append(f"({l}, {r})")
        return ans
