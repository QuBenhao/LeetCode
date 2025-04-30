import solution
from typing import *
from python.object_libs import call_method
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = MyCalendarThree()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class Node:
    __slots__ = ["left", "right", "val", "lazy"]  # 优化内存

    def __init__(self):
        self.left = None
        self.right = None
        self.val = 0
        self.lazy = 0


class DynamicSegmentTree:
    def __init__(self, start, end):
        self.root = Node()
        self.start = start  # 区间左端点
        self.end = end  # 区间右端点
    
    def _push_up(self, node):
        node.val = max(node.left.val, node.right.val)

    def _push_down(self, node, l, r):
        # 动态创建子节点并下推惰性标记
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()
        if node.lazy != 0:
            # 更新左子节点
            node.left.val += node.lazy
            node.left.lazy += node.lazy
            # 更新右子节点
            node.right.val += node.lazy
            node.right.lazy += node.lazy
            node.lazy = 0

    def _update(self, node, l, r, ul, ur, val):
        if ul <= l and r <= ur:  # 完全覆盖
            node.val += val
            node.lazy += val
            return
        self._push_down(node, l, r)
        mid = (l + r) // 2
        if ul <= mid:
            self._update(node.left, l, mid, ul, ur, val)
        if ur > mid:
            self._update(node.right, mid + 1, r, ul, ur, val)
        self._push_up(node)

    def update_range(self, l, r, val):
        """区间更新 [l, r] 增加 val"""
        self._update(self.root, self.start, self.end, l, r, val)

    def _query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return node.val
        self._push_down(node, l, r)
        mid = (l + r) // 2
        return max(self._query(node.left, l, mid, ql, qr), self._query(
            node.right, mid + 1, r, ql, qr
        ))

    def query_range(self, l, r):
        """查询区间 [l, r] 的和"""
        return self._query(self.root, self.start, self.end, l, r)


class MyCalendarThree:
    def __init__(self):
        self.tree = DynamicSegmentTree(0, 1e9)

    def book(self, start: int, end: int) -> int:
        self.tree.update_range(start, end - 1, 1)
        return self.tree.query_range(0, 1e9)

"""
class MyCalendarThree:
    def __init__(self):
        self.tree = defaultdict(int)
        self.lazy = defaultdict(int)

    def update(self, start: int, end: int, l: int, r: int, idx: int):
        if r < start or end < l:
            return
        if start <= l and r <= end:
            self.tree[idx] += 1
            self.lazy[idx] += 1
        else:
            mid = (l + r) // 2
            self.update(start, end, l, mid, idx * 2)
            self.update(start, end, mid + 1, r, idx * 2 + 1)
            self.tree[idx] = self.lazy[idx] + max(self.tree[idx * 2], self.tree[idx * 2 + 1])

    def book(self, start: int, end: int) -> int:
        self.update(start, end - 1, 0, 10 ** 9, 1)
        return self.tree[1]
"""
