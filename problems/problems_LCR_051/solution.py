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
        return self.maxPathSum(root0)

    def maxPathSum(self, root: TreeNode) -> int:
        ans = -0x3f3f3f3f
        def dfs(node):
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            nonlocal ans
            ans = max(ans, node.val + left + right)
            return max(max(left, right) + node.val, 0)

        dfs(root)
        return ans
