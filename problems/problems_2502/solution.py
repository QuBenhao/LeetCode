from collections import defaultdict

import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Allocator(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class Node:
    __slots__ = 'pre0', 'suf0', 'max0', 'todo'


class SegTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.t = [Node() for _ in range(2 << (n - 1).bit_length())]
        self.build(1, 0, n - 1)

    def do(self, i: int, l: int, r: int, v: int) -> None:
        size = 0 if v > 0 else r - l + 1
        self.t[i].pre0 = size
        self.t[i].suf0 = size
        self.t[i].max0 = size
        self.t[i].todo = v

    # 下传懒标记
    def spread(self, o: int, l: int, r: int) -> None:
        v = self.t[o].todo
        if v != -1:
            m = (l + r) // 2
            self.do(o * 2, l, m, v)
            self.do(o * 2 + 1, m + 1, r, v)
            self.t[o].todo = -1

    # 初始化线段树
    def build(self, o: int, l: int, r: int) -> None:
        self.do(o, l, r, -1)
        if l == r:
            return
        m = (l + r) // 2
        self.build(o * 2, l, m)
        self.build(o * 2 + 1, m + 1, r)

    # 把区间 [ql, qr] 都置为 v
    def update(self, o: int, l: int, r: int, ql: int, qr: int, v: int) -> None:
        if ql <= l and r <= qr:
            self.do(o, l, r, v)
            return
        self.spread(o, l, r)
        m = (l + r) // 2
        if ql <= m:
            self.update(o * 2, l, m, ql, qr, v)
        if m < qr:
            self.update(o * 2 + 1, m + 1, r, ql, qr, v)

        # 合并左右子树的信息
        lo = self.t[o * 2]
        ro = self.t[o * 2 + 1]
        # 区间前缀连续 0 的个数
        self.t[o].pre0 = lo.pre0
        if lo.pre0 == m - l + 1:
            self.t[o].pre0 += ro.pre0  # 和右子树的 pre0 拼起来
        # 区间后缀连续 0 的个数
        self.t[o].suf0 = ro.suf0
        if ro.suf0 == r - m:
            self.t[o].suf0 += lo.suf0  # 和左子树的 suf0 拼起来
        # 区间最长连续 0 的个数
        self.t[o].max0 = max(lo.max0, ro.max0, lo.suf0 + ro.pre0)

    # 线段树二分，找最左边的区间左端点，满足区间全为 0 且长度 >= size
    # 如果不存在这样的区间，返回 -1
    def find_first(self, o: int, l: int, r: int, size: int) -> int:
        if self.t[o].max0 < size:
            return -1
        if l == r:
            return l
        self.spread(o, l, r)
        m = (l + r) // 2
        idx = self.find_first(o * 2, l, m, size)  # 递归左子树
        if idx < 0:
            # 左子树的后缀 0 个数 + 右子树的前缀 0 个数 >= size
            if self.t[o * 2].suf0 + self.t[o * 2 + 1].pre0 >= size:
                return m - self.t[o * 2].suf0 + 1
            idx = self.find_first(o * 2 + 1, m + 1, r, size)  # 递归右子树
        return idx


class Allocator:
    def __init__(self, n: int):
        self.n = n
        self.tree = SegTree(n)
        self.blocks = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        i = self.tree.find_first(1, 0, self.n - 1, size)
        if i < 0:  # 无法分配内存
            return -1
        # 分配内存 [i, i+size-1]
        self.blocks[mID].append((i, i + size - 1))
        self.tree.update(1, 0, self.n - 1, i, i + size - 1, 1)
        return i

    def freeMemory(self, mID: int) -> int:
        ans = 0
        for l, r in self.blocks[mID]:
            ans += r - l + 1
            self.tree.update(1, 0, self.n - 1, l, r, 0)  # 释放内存
        del self.blocks[mID]
        return ans

