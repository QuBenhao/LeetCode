import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numOfWays(test_input)

    def numOfWays(self, n: int) -> int:
        m = [[5, -2], [1, 0]]
        f1 = [[12], [3]]
        fn = pow_mul(m, n - 1, f1)
        return fn[0][0]

MOD = 10**9+7

# a @ b，其中 @ 是矩阵乘法
def mul(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    return [[sum(x * y for x, y in zip(row, col)) % MOD for col in zip(*b)]
            for row in a]

# a^n @ f0
def pow_mul(a: List[List[int]], n: int, f0: List[List[int]]) -> List[List[int]]:
    res = f0
    while n:
        if n & 1:
            res = mul(a, res)
        a = mul(a, a)
        n >>= 1
    return res
