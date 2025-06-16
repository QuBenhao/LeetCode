from math import comb
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countGoodArrays(*test_input)

    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        # 第一个选择有m种; 后面相等共享选择是1，不相等共享选择是m-1，有k个1, n-k-1个m-1
        # 我们要从n-1个位置中选择k个位置放1，其余放m-1
        mod = 10**9 + 7
        return (((m * pow(m-1, n-k-1, mod)) % mod) * comb(n-1, k)) % mod
