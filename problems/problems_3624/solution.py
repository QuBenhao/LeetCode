import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.popcountDepth(*test_input)

    def popcountDepth(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def pop_count_depth(x):
            cost = 0
            while x > 1:
                cost += 1
                x = bin(x).count('1')
            return cost

        n = len(nums)
        fenwick_trees = [FenwickTree(n) for _ in range(6)]
        for i, num in enumerate(nums):
            depth = pop_count_depth(num)
            fenwick_trees[depth].update(i + 1, 1)
        result = []
        for q in queries:
            if q[0] == 1:
                result.append(fenwick_trees[q[3]].range_query(q[1]+1, q[2]+1))
            else:
                idx, val = q[1], q[2]
                old_depth = pop_count_depth(nums[idx])
                new_depth = pop_count_depth(val)
                nums[idx] = val
                if old_depth != new_depth:
                    fenwick_trees[old_depth].update(idx + 1, -1)
                    fenwick_trees[new_depth].update(idx + 1, 1)
        return result


class FenwickTree:
    def __init__(self, size: int):
        self.n = size
        self.tree = [0] * (self.n + 1)  # 索引从1开始

    def lowbit(self, x: int) -> int:
        return x & (-x)

    def update(self, idx: int, delta: int) -> None:
        """ 单点更新：a[idx] += delta """
        while idx <= self.n:
            self.tree[idx] += delta
            idx += self.lowbit(idx)

    def query(self, idx: int) -> int:
        """ 查询前缀和：a[1] + a[2] + ... + a[idx] """
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= self.lowbit(idx)
        return res

    def range_query(self, l: int, r: int) -> int:
        """ 区间查询：a[l] + a[l+1] + ... + a[r] """
        return self.query(r) - self.query(l - 1)
