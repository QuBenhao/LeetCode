from math import log10

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.lexicalOrder(test_input)

    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        j = 1
        for i in range(n):
            ans.append(j)
            if j * 10 <= n: # Multiply by 10 whenever possible
                j *= 10
            else:
                while j % 10 == 9 or j + 1 > n: # The current prefix is exhausted; divide by 10 to return to the parent
                    j //= 10
                j += 1 # Next node
        return ans
