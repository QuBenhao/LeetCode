from typing import *

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numOfUnplacedFruits(*test_input)

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 0
        for f in fruits:
            for i, b in enumerate(baskets):
                if b >= f:
                    baskets[i] = 0
                    break
            else:
                ans += 1
        return ans
