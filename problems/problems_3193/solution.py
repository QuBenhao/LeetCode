import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfPermutations(*test_input)

    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 1_000_000_007
        req = [-1] * n
        req[0] = 0
        for end, cnt in requirements:
            req[end] = cnt
        if req[0]:
            return 0

        m = max(req)
        f = [0] * (m + 1)
        f[0] = 1
        for i in range(1, n):
            mx = m if req[i] < 0 else req[i]
            r = req[i - 1]
            if r >= 0:
                for j in range(m + 1):
                    f[j] = f[r] if r <= j <= min(i + r, mx) else 0
            else:
                for j in range(1, mx + 1):  # 计算前缀和
                    f[j] = (f[j] + f[j - 1]) % MOD
                for j in range(mx, i, -1):  # 计算子数组和
                    f[j] = (f[j] - f[j - i - 1]) % MOD
        return f[req[-1]]
