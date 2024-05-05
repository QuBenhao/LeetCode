import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.decrypt(*test_input)

    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans
        s = sum(code[1:k+1] if k > 0 else code[k:])
        for i in range(n):
            ans[i] = s
            s += code[i % n] - code[(i + k) % n] if k < 0 else code[(i + k + 1) % n] - code[(i + 1) % n]
        return ans
