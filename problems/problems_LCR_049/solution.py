import solution
from typing import *
from python.object_libs import list_to_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0 = test_input
        root0 = list_to_tree(nums0)
        return self.sumNumbers(root0)

    def sumNumbers(self, root: TreeNode) -> int:
        ans = 0
        def dfs(node, num):
            if not node:
                return
            num = num * 10 + node.val
            if not node.left and not node.right:
                nonlocal ans
                ans += num
                return
            dfs(node.left, num)
            dfs(node.right, num)

        dfs(root, 0)
        return ans
