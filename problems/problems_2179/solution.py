import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.goodTriplets(*test_input)

    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        class FenwickTree:
            def __init__(self, n: int):
                self.tree = [0] * (n + 1)  # 使用下标 1 到 n

            # a[i] 增加 val
            # 1 <= i <= n
            def update(self, i: int, val: int) -> None:
                while i < len(self.tree):
                    self.tree[i] += val
                    i += i & -i

            # 计算前缀和 a[1] + ... + a[i]
            # 1 <= i <= n
            def pre(self, i: int) -> int:
                res = 0
                while i > 0:
                    res += self.tree[i]
                    i &= i - 1
                return res

        n = len(nums1)
        p = [0] * n
        for i, x in enumerate(nums1):
            p[x] = i

        ans = 0
        t = FenwickTree(n)
        for i, y in enumerate(nums2):
            y = p[y]
            less = t.pre(y)
            ans += less * (n - 1 - y - (i - less))
            t.update(y + 1, 1)
        return ans
