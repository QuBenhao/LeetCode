import solution
from typing import *
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestOverlap(*test_input)

    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        # 平移量由「img1 的一个 1 与 img2 的一个 1 落在同一格」唯一确定：
        # 偏移 = 两者坐标之差，同一个偏移对上的对数就是该偏移的重叠数。
        n = len(img1)
        a = [(i, j) for i, row in enumerate(img1) for j, v in enumerate(row) if v]
        b = [(i, j) for i, row in enumerate(img2) for j, v in enumerate(row) if v]
        # 点对计数代价正比 |a|·|b|，稀疏时极快；逐行 bitset 代价约 4n³，与密度无关。
        # 实测切换点 |a|·|b| ≈ 2.4n³（n=30 约 6.5e4，n=15 约 8.1e3，Python 实测）。
        if len(a) * len(b) <= 2.4 * n ** 3:
            return max(Counter((i - x, j - y) for i, j in a for x, y in b).values(), default=0)
        return self._by_bitset(img1, img2)

    @staticmethod
    def _by_bitset(img1: List[List[int]], img2: List[List[int]]) -> int:
        # 每行压成整数：平移变成移位，重叠数变成按位与后的 bit_count
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
