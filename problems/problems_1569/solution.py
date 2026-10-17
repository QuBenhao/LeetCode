import sys
from math import comb

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numOfWays(test_input)

    def numOfWays(self, nums: list[int]) -> int:
        """建出 BST，再在树上递归计数。

        核心：一棵子树的所有合法重排，只要求「父节点排在子节点之前」。
        左右子树各自排好之后，剩下的唯一自由度是把两条序列交错，
        即 C(ls + rs, ls)，所以递归必须同时带出「方案数」和「子树大小」。
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        sys.setrecursionlimit(max(10000, n + 100))  # 退化成链时递归深度可达 n

        class TreeNode:
            __slots__ = ("val", "left", "right")

            def __init__(self, val=0, left=None, right=None):
                self.val = val
                self.left = left
                self.right = right

        root = TreeNode(nums[0])

        def add_node(val, cur_root: TreeNode):
            if not cur_root:
                return TreeNode(val)
            if val < cur_root.val:
                cur_root.left = add_node(val, cur_root.left)
            else:
                cur_root.right = add_node(val, cur_root.right)
            return cur_root

        for i in range(1, n):
            add_node(nums[i], root)

        def dfs(node):
            """返回 (这棵子树的合法重排数, 节点数)"""
            if node is None:
                return 1, 0  # 空树是乘法单位元，叶子因此不需要特判
            lw, ls = dfs(node.left)
            rw, rs = dfs(node.right)
            # 左右内部顺序各自定好，只需交错合并：从 ls+rs 个位置挑 ls 个给左子树
            return comb(ls + rs, ls) * lw % MOD * rw % MOD, ls + rs + 1

        # 题目要求「重新排序」，扣掉原数组本身这一种
        return (dfs(root)[0] - 1) % MOD

    def numOfWaysByValueRange(self, nums: list[int]) -> int:
        """备选：不建树，直接对值域区间递归。

        nums 是 1..n 的排列，所以一棵 BST 子树恰好对应一段连续值域 [lo, hi]：
        区间内的值插入时都会落进这棵子树。子树的根 = 区间里最早插入的那个值。
        省掉了树对象，但 Python 下 min(range, key=...) 的调用开销让它实测略慢。
        """
        MOD = 10 ** 9 + 7
        n = len(nums)
        sys.setrecursionlimit(max(10000, n + 100))

        pos = {v: i for i, v in enumerate(nums)}  # 值 -> 在 nums 中的下标

        def dfs(lo: int, hi: int) -> int:
            if hi - lo <= 1:  # 0 / 1 / 2 个节点，只有一种相对顺序
                return 1
            root = min(range(lo, hi + 1), key=pos.__getitem__)  # 最早插入者作根
            ls, rs = root - lo, hi - root
            return comb(ls + rs, ls) * dfs(lo, root - 1) % MOD * dfs(root + 1, hi) % MOD

        return (dfs(1, n) - 1) % MOD
