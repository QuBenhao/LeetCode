import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestBalanced(test_input)

    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        t = LazySegmentTree(n + 1)

        last = {}  # Last occurrence of each element in nums
        ans = cur_sum = 0
        for i, x in enumerate(nums, 1):
            v = 1 if x % 2 else -1
            j = last.get(x, 0)
            if j == 0:  # First occurrence of x
                cur_sum += v
                t.update(i, n, v)  # Increase sum[i:] by v
            else:  # Encountered x again
                t.update(j, i - 1, -v)  # Undo the previous increase to sum[j:i]
            last[x] = i

            # Optimize i-1 to i-1-ans: searching indices > i-1-ans cannot improve the answer
            j = t.find_first(0, i - 1 - ans, cur_sum)
            if j >= 0:
                ans = i - j  # If found, the answer must increase
        return ans


# Handwritten min and max are faster
min = lambda a, b: b if b < a else a
max = lambda a, b: b if b > a else a

class Node:
    __slots__ = 'min', 'max', 'todo'

    def __init__(self):
        self.min = self.max = self.todo = 0

class LazySegmentTree:
    def __init__(self, n: int):
        self._n = n
        self._tree = [Node() for _ in range(2 << (n - 1).bit_length())]

    # Apply the lazy tag to the subtree rooted at node
    def _apply(self, node: int, todo: int) -> None:
        cur = self._tree[node]
        cur.min += todo
        cur.max += todo
        cur.todo += todo

    # Push the current node's lazy tag down to its left and right children
    def _spread(self, node: int) -> None:
        todo = self._tree[node].todo
        if todo == 0:  # No information needs to be pushed down
            return
        self._apply(node * 2, todo)
        self._apply(node * 2 + 1, todo)
        self._tree[node].todo = 0  # Finished pushing down

    # Merge the left and right children's min and max into the current node
    def _maintain(self, node: int) -> None:
        l_node = self._tree[node * 2]
        r_node = self._tree[node * 2 + 1]
        self._tree[node].min = min(l_node.min, r_node.min)
        self._tree[node].max = max(l_node.max, r_node.max)

    def _update(self, node: int, l: int, r: int, ql: int, qr: int, f: int) -> None:
        if ql <= l and r <= qr:  # The current subtree lies entirely within [ql, qr]
            self._apply(node, f)
            return
        self._spread(node)
        m = (l + r) // 2
        if ql <= m:  # Update the left subtree
            self._update(node * 2, l, m, ql, qr, f)
        if qr > m:  # Update the right subtree
            self._update(node * 2 + 1, m + 1, r, ql, qr, f)
        self._maintain(node)

    def _find_first(self, node: int, l: int, r: int, ql: int, qr: int, target: int) -> int:
        if l > qr or r < ql or not self._tree[node].min <= target <= self._tree[node].max:
            return -1
        if l == r:
            return l
        self._spread(node)
        m = (l + r) // 2
        idx = self._find_first(node * 2, l, m, ql, qr, target)
        if idx < 0:
            # Search the right subtree
            idx = self._find_first(node * 2 + 1, m + 1, r, ql, qr, target)
        return idx

    # Use f to update each sum[i] in [ql, qr]
    # 0 <= ql <= qr <= n-1
    # Time complexity O(log n)
    def update(self, ql: int, qr: int, f: int) -> None:
        self._update(1, 0, self._n - 1, ql, qr, f)

    # Query the index of the first element equal to target in [ql, qr]
    # Return -1 if not found
    # 0 <= ql <= qr <= n-1
    # Time complexity O(log n)
    def find_first(self, ql: int, qr: int, target: int) -> int:
        return self._find_first(1, 0, self._n - 1, ql, qr, target)
