import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = MyCalendar()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class Node:
    __slots__ = ['left', 'right', 'val', 'lazy']  # 优化内存

    def __init__(self):
        self.left = None
        self.right = None
        self.val = 0
        self.lazy = 0  # 惰性标记（用于区间更新）


class DynamicSegmentTree:
    def __init__(self, start, end):
        self.root = Node()
        self.start = start  # 区间左端点
        self.end = end  # 区间右端点

    def _push_down(self, node):
        # 动态创建子节点并下推惰性标记
        if node.left is None:
            node.left = Node()
        if node.right is None:
            node.right = Node()
        if node.lazy != 0:
            # 更新左子节点
            node.left.val = node.lazy
            node.left.lazy = node.lazy
            # 更新右子节点
            node.right.val = node.lazy
            node.right.lazy = node.lazy
            node.lazy = 0

    def _update(self, node, l, r, ul, ur, val):
        if ul <= l and r <= ur:  # 完全覆盖
            node.val = val
            node.lazy = val
            return
        self._push_down(node)
        mid = (l + r) // 2
        if ul <= mid:
            self._update(node.left, l, mid, ul, ur, val)
        if ur > mid:
            self._update(node.right, mid + 1, r, ul, ur, val)
        node.val = max(node.left.val, node.right.val)

    def update_range(self, l, r, val):
        """区间更新 [l, r] 增加 val"""
        self._update(self.root, self.start, self.end, l, r, val)

    def _query(self, node, l, r, ql, qr):
        if qr < l or r < ql:
            return 0
        if ql <= l and r <= qr:
            return node.val
        self._push_down(node)
        mid = (l + r) // 2
        return max(self._query(node.left, l, mid, ql, qr),
            self._query(node.right, mid + 1, r, ql, qr))

    def query_range(self, l, r):
        """查询区间 [l, r] 的和"""
        return self._query(self.root, self.start, self.end, l, r)


class MyCalendar:
    def __init__(self):
        self.seg_tree = DynamicSegmentTree(0, 10**9)  # 时间范围是 [0, 10^9]

    def book(self, start: int, end: int) -> bool:
        if self.seg_tree.query_range(start, end-1):
            return False
        self.seg_tree.update_range(start, end-1, 1)
        return True
