import solution
from typing import *
from object_libs import list_to_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root = list_to_tree(test_input)
        return self.sumNumbers(root)

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, v):
            nv = 10 * v + node.val
            if not node.left and not node.right:
                return nv
            ans = 0
            if node.left:
                ans += dfs(node.left, nv)
            if node.right:
                ans += dfs(node.right, nv)
            return ans

        return dfs(root, 0)
