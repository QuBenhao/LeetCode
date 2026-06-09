from bisect import bisect_left
from collections import deque

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxTotalValue(*test_input)

    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # 二分 + 滑动窗口 + 单调队列
        def check(low_d: int) -> bool:
            low_d += 1
            # 1438. 绝对差不超过限制的最长连续子数组（改成求子数组个数）
            min_q = deque()
            max_q = deque()
            cnt = left = 0

            for i, x in enumerate(nums):
                # 1. 右边入
                while min_q and x <= nums[min_q[-1]]:
                    min_q.pop()
                min_q.append(i)

                while max_q and x >= nums[max_q[-1]]:
                    max_q.pop()
                max_q.append(i)

                # 2. 左边出
                while nums[max_q[0]] - nums[min_q[0]] >= low_d:
                    left += 1
                    if min_q[0] < left:  # 队首不在窗口中
                        min_q.popleft()
                    if max_q[0] < left:  # 队首不在窗口中
                        max_q.popleft()

                cnt += left
                if cnt >= k:
                    return False
            return True

        low_d = bisect_left(range(max(nums) - min(nums)), True, key=check)

        # 单调栈
        n = len(nums)
        left_less_eq = [0] * n
        left_great_eq = [0] * n
        st1 = [-1]  # 哨兵
        st2 = [-1]
        for i, x in enumerate(nums):
            while len(st1) > 1 and nums[st1[-1]] > x:
                st1.pop()
            left_less_eq[i] = st1[-1]
            st1.append(i)

            while len(st2) > 1 and nums[st2[-1]] < x:
                st2.pop()
            left_great_eq[i] = st2[-1]
            st2.append(i)

        # Lazy 线段树
        t = LazySegmentTree(n)
        cnt = s = 0
        for i, x in enumerate(nums):
            t.update(left_less_eq[i] + 1, i, (x, -1))
            t.update(left_great_eq[i] + 1, i, (-1, x))
            l = t.find_last(0, i, lambda v: v[3] - v[2] >= low_d)
            if l >= 0:
                cnt += l + 1
                d = t.query(0, l)
                s += d[1] - d[0]

        return s - (cnt - k) * low_d  # 减掉多算的


class Node:
    # val = [sum_min, sum_max, l_min, l_max]
    # todo = [todo_min, todo_max]
    __slots__ = 'val', 'todo'


class LazySegmentTree:
    # 懒标记初始值
    _TODO_INIT = [-1, -1]

    def __init__(self, n: int):
        # 线段树维护一个长为 n 的数组（下标从 0 到 n-1）
        self._n = n
        self._tree = [Node() for _ in range(2 << (n - 1).bit_length())]
        self._build(1, 0, n - 1)

    # 合并两个 val
    def _merge_val(self, a: List[int], b: List[int]) -> List[int]:
        return [a[0] + b[0], a[1] + b[1], a[2], a[3]]

    # 把懒标记作用到 node 子树（本例为区间加）
    def _apply(self, node: int, l: int, r: int, todo) -> None:
        cur = self._tree[node]
        # 计算 tree[node] 区间的整体变化
        todo_min, todo_max = todo
        if todo_min >= 0:
            cur.val[0] = todo_min * (r - l + 1)
            cur.val[2] = todo_min
            cur.todo[0] = todo_min
        if todo_max >= 0:
            cur.val[1] = todo_max * (r - l + 1)
            cur.val[3] = todo_max
            cur.todo[1] = todo_max

    # 把当前节点的懒标记下传给左右儿子
    def _spread(self, node: int, l: int, r: int) -> None:
        todo = self._tree[node].todo
        if todo == self._TODO_INIT:  # 没有需要下传的信息
            return
        m = (l + r) // 2
        self._apply(node * 2, l, m, todo)
        self._apply(node * 2 + 1, m + 1, r, todo)
        todo[:] = self._TODO_INIT[:]  # 下传完毕

    # 合并左右儿子的 val 到当前节点的 val
    def _maintain(self, node: int) -> None:
        self._tree[node].val = self._merge_val(self._tree[node * 2].val, self._tree[node * 2 + 1].val)

    # 初始化线段树
    # 时间复杂度 O(n)
    def _build(self, node: int, l: int, r: int) -> None:
        self._tree[node].val = [0] * 4
        self._tree[node].todo = self._TODO_INIT[:]
        if l == r:  # 叶子
            return
        m = (l + r) // 2
        self._build(node * 2, l, m)  # 初始化左子树
        self._build(node * 2 + 1, m + 1, r)  # 初始化右子树
        self._maintain(node)

    def _update(self, node: int, l: int, r: int, ql: int, qr: int, f: Tuple[int, int]) -> None:
        if ql <= l and r <= qr:  # 当前子树完全在 [ql, qr] 内
            self._apply(node, l, r, f)
            return
        self._spread(node, l, r)
        m = (l + r) // 2
        if ql <= m:  # 更新左子树
            self._update(node * 2, l, m, ql, qr, f)
        if qr > m:  # 更新右子树
            self._update(node * 2 + 1, m + 1, r, ql, qr, f)
        self._maintain(node)

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> List[int]:
        if ql <= l and r <= qr:  # 当前子树完全在 [ql, qr] 内
            return self._tree[node].val
        self._spread(node, l, r)
        m = (l + r) // 2
        if qr <= m:  # [ql, qr] 在左子树
            return self._query(node * 2, l, m, ql, qr)
        if ql > m:  # [ql, qr] 在右子树
            return self._query(node * 2 + 1, m + 1, r, ql, qr)
        l_res = self._query(node * 2, l, m, ql, qr)
        r_res = self._query(node * 2 + 1, m + 1, r, ql, qr)
        return self._merge_val(l_res, r_res)

    def _find_last(self, node: int, l: int, r: int, ql: int, qr: int, f: Callable[[List[int]], int]) -> int:
        if l > qr or r < ql or not f(self._tree[node].val):
            return -1
        if l == r:
            return l
        self._spread(node, l, r)
        m = (l + r) // 2
        idx = self._find_last(node * 2 + 1, m + 1, r, ql, qr, f)
        if idx < 0:
            idx = self._find_last(node * 2, l, m, ql, qr, f)
        return idx

    # 用 f 更新 [ql, qr] 中的每个 a[i]
    # 0 <= ql <= qr <= n-1
    # 时间复杂度 O(log n)
    def update(self, ql: int, qr: int, f: Tuple[int, int]) -> None:
        self._update(1, 0, self._n - 1, ql, qr, f)

    # 返回用 _merge_val 合并所有 a[i] 的计算结果，其中 i 在闭区间 [ql, qr] 中
    # 0 <= ql <= qr <= n-1
    # 时间复杂度 O(log n)
    def query(self, ql: int, qr: int) -> List[int]:
        return self._query(1, 0, self._n - 1, ql, qr)

    # 返回 [ql, qr] 内最后一个满足 f 的下标
    # 0 <= ql <= qr <= n-1
    # 时间复杂度 O(log n)
    def find_last(self, ql: int, qr: int, f: Callable[[List[int]], int]) -> int:
        return self._find_last(1, 0, self._n - 1, ql, qr, f)
