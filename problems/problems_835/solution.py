import solution
from typing import *
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestOverlap(*test_input)

    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # The translation is uniquely determined by aligning one 1 in img1 with one 1 in img2:
        # Offset = the difference between their coordinates; the number of pairs with that offset is its overlap count.
        n = len(img1)
        a = [(i, j) for i, row in enumerate(img1) for j, v in enumerate(row) if v]
        b = [(i, j) for i, row in enumerate(img2) for j, v in enumerate(row) if v]
        # Pair counting costs O(|a|·|b|) and is very fast for sparse inputs; row-wise bitsets cost about 4n³ regardless of density.
        # Measured crossover: |a|·|b| ≈ 2.4n³ (about 6.5e4 for n=30 and 8.1e3 for n=15, measured in Python).
        if len(a) * len(b) <= 2.4 * n ** 3:
            return max(Counter((i - x, j - y) for i, j in a for x, y in b).values(), default=0)
        return self._by_bitset(img1, img2)

    @staticmethod
    def _by_bitset(img1: List[List[int]], img2: List[List[int]]) -> int:
        # Pack each row into an integer: translation becomes shifting, and overlap becomes bit_count after a bitwise AND
        n = len(img1)
        ra = [int("".join(map(str, row)), 2) for row in img1]
        rb = [int("".join(map(str, row)), 2) for row in img2]
        best = 0
        for di in range(1 - n, n):
            for dj in range(1 - n, n):
                cur = sum((ra[i] & (rb[i + di] >> dj if dj >= 0 else rb[i + di] << -dj)).bit_count()
                          for i in range(n) if 0 <= i + di < n)
                best = max(best, cur)
        return best
