import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.validStrings(test_input)

    def validStrings(self, n: int) -> List[str]:
        ans = []
        path = [''] * n

        def backtrack(i: int):
            if i == n:
                ans.append("".join(path))
                return

            if i == 0 or path[i-1] == '1':
                path[i] = '0'
                backtrack(i+1)

            path[i] = '1'
            backtrack(i+1)

        backtrack(0)
        return ans
