import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.recoverOrder(*test_input)

    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans = []
        s = set(friends)
        for o in order:
            if o in s:
                ans.append(o)
        return ans
