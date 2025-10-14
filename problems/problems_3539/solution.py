import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.magicalSum(*test_input)

    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n = len(nums)
        pow_v = [[1] * (m + 1) for _ in range(n)]
        for i, v in enumerate(nums):
            for j in range(1, m + 1):
                pow_v[i][j] = pow_v[i][j - 1] * v % MOD

        f = [[[[0] * (k + 1) for _ in range(m // 2 + 1)] for _ in range(m + 1)] for _ in range(n + 1)]
        for x in range(m // 2 + 1):
            c1 = x.bit_count()
            if c1 <= k:
                f[n][0][x][c1] = 1

        for i in range(n - 1, -1, -1):
            for left_m in range(m + 1):
                for x in range(m // 2 + 1):
                    for left_k in range(k + 1):
                        res = 0
                        for j in range(min(left_m, m - x) + 1):
                            bit = (x + j) & 1
                            if bit <= left_k:
                                r = f[i + 1][left_m - j][(x + j) >> 1][left_k - bit]
                                res += r * pow_v[i][j] * inv_f[j]
                        f[i][left_m][x][left_k] = res % MOD
        return f[0][m][0][k] * fac[m] % MOD


MOD = 1_000_000_007
MX = 31

fac = [0] * MX  # fac[i] = i!
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD

inv_f = [0] * MX  # inv_f[i] = i!^-1
inv_f[-1] = pow(fac[-1], -1, MOD)
for i in range(MX - 1, 0, -1):
    inv_f[i - 1] = inv_f[i] * i % MOD
