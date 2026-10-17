from math import comb

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numOfWays(test_input)

    def numOfWays(self, nums: list[int]) -> int:
        class TreeNode:
            __slots__ = 'val', 'left', 'right'
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

        for i in range(1, len(nums)):
            add_node(nums[i], root)

        # 树只决定父节点在子节点之前构造到数组中，统计方案数
        def dfs(node):
            if not node:
                return 1, 0 # 方案数, 树大小
            la, ls = dfs(node.left)
            ra, rs = dfs(node.right)
            # 当前节点的方案数由 左子树的方案数 * 右子树的方案数 * 左右子树抢位置的组合数构成
            # 左右子树相互是不会影响的，comb(ls + rs, ls)相当于左子树选择了哪些空位（剩下的自然是右子树的)
            return comb(ls + rs, ls) * la % MOD * ra % MOD, ls + rs + 1

        return dfs(root)[0] - 1

MOD = 10**9 + 7
