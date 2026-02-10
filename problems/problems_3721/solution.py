import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestBalanced(test_input)

    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        t = LazySegmentTree(n + 1)

        last = {}  # nums 的元素上一次出现的位置
        ans = cur_sum = 0
        for i, x in enumerate(nums, 1):
            v = 1 if x % 2 else -1
            j = last.get(x, 0)
            if j == 0:  # 首次遇到 x
                cur_sum += v
                t.update(i, n, v)  # sum[i:] 增加 v
            else:  # 再次遇到 x
                t.update(j, i - 1, -v)  # 撤销之前对 sum[j:i] 的增加
            last[x] = i

            # 把 i-1 优化成 i-1-ans，因为在下标 > i-1-ans 中搜索是没有意义的，不会把答案变大
            j = t.find_first(0, i - 1 - ans, cur_sum)
            if j >= 0:
                ans = i - j  # 如果找到了，那么答案肯定会变大
        return ans


# 手写 min max 更快
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

    # 把懒标记作用到 node 子树
    def _apply(self, node: int, todo: int) -> None:
        cur = self._tree[node]
        cur.min += todo
        cur.max += todo
        cur.todo += todo

    # 把当前节点的懒标记下传给左右儿子
    def _spread(self, node: int) -> None:
        todo = self._tree[node].todo
        if todo == 0:  # 没有需要下传的信息
            return
        self._apply(node * 2, todo)
        self._apply(node * 2 + 1, todo)
        self._tree[node].todo = 0  # 下传完毕

    # 合并左右儿子的 min max 到当前节点
    def _maintain(self, node: int) -> None:
        l_node = self._tree[node * 2]
        r_node = self._tree[node * 2 + 1]
        self._tree[node].min = min(l_node.min, r_node.min)
        self._tree[node].max = max(l_node.max, r_node.max)

    def _update(self, node: int, l: int, r: int, ql: int, qr: int, f: int) -> None:
        if ql <= l and r <= qr:  # 当前子树完全在 [ql, qr] 内
            self._apply(node, f)
            return
        self._spread(node)
        m = (l + r) // 2
        if ql <= m:  # 更新左子树
            self._update(node * 2, l, m, ql, qr, f)
        if qr > m:  # 更新右子树
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
            # 去右子树找
            idx = self._find_first(node * 2 + 1, m + 1, r, ql, qr, target)
        return idx

    # 用 f 更新 [ql, qr] 中的每个 sum[i]
    # 0 <= ql <= qr <= n-1
    # 时间复杂度 O(log n)
    def update(self, ql: int, qr: int, f: int) -> None:
        self._update(1, 0, self._n - 1, ql, qr, f)

    # 查询 [ql, qr] 内第一个等于 target 的元素下标
    # 找不到返回 -1
    # 0 <= ql <= qr <= n-1
    # 时间复杂度 O(log n)
    def find_first(self, ql: int, qr: int, target: int) -> int:
        return self._find_first(1, 0, self._n - 1, ql, qr, target)
