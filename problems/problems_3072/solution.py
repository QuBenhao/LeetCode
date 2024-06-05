import solution
from typing import *
from bisect import bisect_left


class Fenwick:
    __slots__ = 'tree'

    def __init__(self, n: int):
        self.tree = [0] * n

    # 把下标为 i 的元素增加 v
    def add(self, i: int, v: int) -> None:
        while i < len(self.tree):
            self.tree[i] += v
            i += i & -i

    # 返回下标在 [1,i] 的元素之和
    def pre(self, i: int) -> int:
        res = 0
        while i > 0:
            res += self.tree[i]
            i &= i - 1
        return res


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.resultArray(test_input)

    def resultArray(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(set(nums))
        m = len(sorted_nums)
        a = [nums[0]]
        b = [nums[1]]
        t = Fenwick(m + 1)
        t.add(m - bisect_left(sorted_nums, nums[0]), 1)
        t.add(m - bisect_left(sorted_nums, nums[1]), -1)
        for x in nums[2:]:
            v = m - bisect_left(sorted_nums, x)
            d = t.pre(v - 1)  # 转换成 < v 的元素个数之差
            if d > 0 or d == 0 and len(a) <= len(b):
                a.append(x)
                t.add(v, 1)
            else:
                b.append(x)
                t.add(v, -1)
        return a + b

