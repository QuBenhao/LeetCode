import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countSmaller(test_input)

    def countSmaller(self, nums: List[int]) -> List[int]:
        class FenwickTree:
            def __init__(self, size: int):
                self.n = size
                self.tree = [0] * (self.n + 1)  # Indices start at 1

            def lowbit(self, x: int) -> int:
                return x & (-x)

            def update(self, idx: int, delta: int) -> None:
                """ Point update: a[idx] += delta """
                while idx <= self.n:
                    self.tree[idx] += delta
                    idx += self.lowbit(idx)

            def query(self, idx: int) -> int:
                """ Query the prefix sum: a[1] + a[2] + ... + a[idx] """
                res = 0
                while idx > 0:
                    res += self.tree[idx]
                    idx -= self.lowbit(idx)
                return res

            def range_query(self, l: int, r: int) -> int:
                """ Range query: a[l] + a[l+1] + ... + a[r] """
                return self.query(r) - self.query(l-1)

        n = len(nums)
        idx_map = {num: i for i, num in enumerate(sorted(set(nums)))}
        tree = FenwickTree(len(idx_map))
        ans = [0] * n
        for i in range(n - 1, -1, -1):
            idx = idx_map[nums[i]]
            ans[i] = tree.query(idx)
            tree.update(idx+1, 1)
        return ans
