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

    # Push down lazy tags
    def spread(self, o: int, l: int, r: int) -> None:
        v = self.t[o].todo
        if v != -1:
            m = (l + r) // 2
            self.do(o * 2, l, m, v)
            self.do(o * 2 + 1, m + 1, r, v)
            self.t[o].todo = -1

    # Initialize the segment tree
    def build(self, o: int, l: int, r: int) -> None:
        self.do(o, l, r, -1)
        if l == r:
            return
        m = (l + r) // 2
        self.build(o * 2, l, m)
        self.build(o * 2 + 1, m + 1, r)

    # Set every value in [ql, qr] to v
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

        # Merge information from the left and right subtrees
        lo = self.t[o * 2]
        ro = self.t[o * 2 + 1]
        # Number of consecutive zeros at the start of the interval
        self.t[o].pre0 = lo.pre0
        if lo.pre0 == m - l + 1:
            self.t[o].pre0 += ro.pre0  # Join with the right subtree's pre0
        # Number of consecutive zeros at the end of the interval
        self.t[o].suf0 = ro.suf0
        if ro.suf0 == r - m:
            self.t[o].suf0 += lo.suf0  # Join with the left subtree's suf0
        # Longest run of consecutive zeros in the interval
        self.t[o].max0 = max(lo.max0, ro.max0, lo.suf0 + ro.pre0)

    # Binary-search the segment tree for the leftmost start of an all-zero interval with length >= size
    # Return -1 if no such interval exists
    def find_first(self, o: int, l: int, r: int, size: int) -> int:
        if self.t[o].max0 < size:
            return -1
        if l == r:
            return l
        self.spread(o, l, r)
        m = (l + r) // 2
        idx = self.find_first(o * 2, l, m, size)  # Recurse into the left subtree
        if idx < 0:
            # Left subtree's zero suffix length + right subtree's zero prefix length >= size
            if self.t[o * 2].suf0 + self.t[o * 2 + 1].pre0 >= size:
                return m - self.t[o * 2].suf0 + 1
            idx = self.find_first(o * 2 + 1, m + 1, r, size)  # Recurse into the right subtree
        return idx


class Allocator:
    def __init__(self, n: int):
        self.n = n
        self.tree = SegTree(n)
        self.blocks = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        i = self.tree.find_first(1, 0, self.n - 1, size)
        if i < 0:  # Cannot allocate memory
            return -1
        # Allocate memory [i, i+size-1]
        self.blocks[mID].append((i, i + size - 1))
        self.tree.update(1, 0, self.n - 1, i, i + size - 1, 1)
        return i

    def freeMemory(self, mID: int) -> int:
        ans = 0
        for l, r in self.blocks[mID]:
            ans += r - l + 1
            self.tree.update(1, 0, self.n - 1, l, r, 0)  # Free memory
        del self.blocks[mID]
        return ans

