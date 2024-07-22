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
        return self.diameterOfBinaryTree(root0)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            nonlocal ans
            ans = max(ans, max(ans, left + right + 1))
            return max(left, right) + 1

        dfs(root)
        return ans - 1
