import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.lengthAfterTransformations(*test_input)

    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 10 ** 9 + 7

        matrix = [[0] * 26 for _ in range(26)]
        for i, c in enumerate(nums):
            for j in range(i + 1, i + c + 1):
                matrix[j % 26][i] += 1
        f = [[0] for _ in range(26)]
        for c in s:
            f[ord(c) - ord('a')][0] += 1

        # 矩阵快速幂
        # a @ b，其中 @ 是矩阵乘法
        def mul(a: List[List[int]], b: List[List[int]], MOD: int) -> List[List[int]]:
            return [[sum(x * y for x, y in zip(row, col)) % MOD for col in zip(*b)]
                    for row in a]

        # a^n @ f0
        def pow_mul(a: List[List[int]], n: int, f0: List[List[int]], MOD: int) -> List[List[int]]:
            res = f0
            while n:
                if n & 1:
                    res = mul(a, res, MOD)
                a = mul(a, a, MOD)
                n >>= 1
            return res

        f = pow_mul(matrix, t, f, mod)
        return sum(c[0] for c in f) % mod
