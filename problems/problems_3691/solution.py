from bisect import bisect_left
from collections import deque

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxTotalValue(*test_input)

    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # Binary search + sliding window + monotonic deque
        def check(low_d: int) -> bool:
            low_d += 1
            # 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit (modified to count subarrays)
            min_q = deque()
            max_q = deque()
            cnt = left = 0

            for i, x in enumerate(nums):
                # 1. Add on the right
                while min_q and x <= nums[min_q[-1]]:
                    min_q.pop()
                min_q.append(i)

                while max_q and x >= nums[max_q[-1]]:
                    max_q.pop()
                max_q.append(i)

                # 2. Remove on the left
                while nums[max_q[0]] - nums[min_q[0]] >= low_d:
                    left += 1
                    if min_q[0] < left:  # The front of the deque is outside the window
                        min_q.popleft()
                    if max_q[0] < left:  # The front of the deque is outside the window
                        max_q.popleft()

                cnt += left
                if cnt >= k:
                    return False
            return True

        low_d = bisect_left(range(max(nums) - min(nums)), True, key=check)

        # Monotonic stack
        n = len(nums)
        left_less_eq = [0] * n
        left_great_eq = [0] * n
        st1 = [-1]  # Sentinel
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

        # Lazy segment tree
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

        return s - (cnt - k) * low_d  # Subtract the overcounted amount


class Node:
    # val = [sum_min, sum_max, l_min, l_max]
    # todo = [todo_min, todo_max]
    __slots__ = 'val', 'todo'


class LazySegmentTree:
    # Initial lazy tag value
    _TODO_INIT = [-1, -1]

    def __init__(self, n: int):
        # The segment tree maintains an array of length n (indices 0 through n-1)
        self._n = n
        self._tree = [Node() for _ in range(2 << (n - 1).bit_length())]
        self._build(1, 0, n - 1)

    # Merge two val values
    def _merge_val(self, a: List[int], b: List[int]) -> List[int]:
        return [a[0] + b[0], a[1] + b[1], a[2], a[3]]

    # Apply the lazy tag to the subtree rooted at node (range addition in this example)
    def _apply(self, node: int, l: int, r: int, todo) -> None:
        cur = self._tree[node]
        # Compute the overall change to the interval represented by tree[node]
        todo_min, todo_max = todo
        if todo_min >= 0:
            cur.val[0] = todo_min * (r - l + 1)
            cur.val[2] = todo_min
            cur.todo[0] = todo_min
        if todo_max >= 0:
            cur.val[1] = todo_max * (r - l + 1)
            cur.val[3] = todo_max
            cur.todo[1] = todo_max

    # Push the current node's lazy tag down to its left and right children
    def _spread(self, node: int, l: int, r: int) -> None:
        todo = self._tree[node].todo
        if todo == self._TODO_INIT:  # No information needs to be pushed down
            return
        m = (l + r) // 2
        self._apply(node * 2, l, m, todo)
        self._apply(node * 2 + 1, m + 1, r, todo)
        todo[:] = self._TODO_INIT[:]  # Finished pushing down

    # Merge the left and right children's val into the current node's val
    def _maintain(self, node: int) -> None:
        self._tree[node].val = self._merge_val(self._tree[node * 2].val, self._tree[node * 2 + 1].val)

    # Initialize the segment tree
    # Time complexity O(n)
    def _build(self, node: int, l: int, r: int) -> None:
        self._tree[node].val = [0] * 4
        self._tree[node].todo = self._TODO_INIT[:]
        if l == r:  # Leaf
            return
        m = (l + r) // 2
        self._build(node * 2, l, m)  # Initialize the left subtree
        self._build(node * 2 + 1, m + 1, r)  # Initialize the right subtree
        self._maintain(node)

    def _update(self, node: int, l: int, r: int, ql: int, qr: int, f: Tuple[int, int]) -> None:
        if ql <= l and r <= qr:  # The current subtree lies entirely within [ql, qr]
            self._apply(node, l, r, f)
            return
        self._spread(node, l, r)
        m = (l + r) // 2
        if ql <= m:  # Update the left subtree
            self._update(node * 2, l, m, ql, qr, f)
        if qr > m:  # Update the right subtree
            self._update(node * 2 + 1, m + 1, r, ql, qr, f)
        self._maintain(node)

    def _query(self, node: int, l: int, r: int, ql: int, qr: int) -> List[int]:
        if ql <= l and r <= qr:  # The current subtree lies entirely within [ql, qr]
            return self._tree[node].val
        self._spread(node, l, r)
        m = (l + r) // 2
        if qr <= m:  # [ql, qr] lies in the left subtree
            return self._query(node * 2, l, m, ql, qr)
        if ql > m:  # [ql, qr] lies in the right subtree
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

    # Use f to update each a[i] in [ql, qr]
    # 0 <= ql <= qr <= n-1
    # Time complexity O(log n)
    def update(self, ql: int, qr: int, f: Tuple[int, int]) -> None:
        self._update(1, 0, self._n - 1, ql, qr, f)

    # Return the result of combining all a[i] with _merge_val, where i is in the closed interval [ql, qr]
    # 0 <= ql <= qr <= n-1
    # Time complexity O(log n)
    def query(self, ql: int, qr: int) -> List[int]:
        return self._query(1, 0, self._n - 1, ql, qr)

    # Return the last index in [ql, qr] satisfying f
    # 0 <= ql <= qr <= n-1
    # Time complexity O(log n)
    def find_last(self, ql: int, qr: int, f: Callable[[List[int]], int]) -> int:
        return self._find_last(1, 0, self._n - 1, ql, qr, f)
