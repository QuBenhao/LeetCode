import solution
from typing import *
from python.object_libs import list_to_tree
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0 = test_input
        root0 = list_to_tree(nums0)
        return self.maxPathSum(root0)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0  # No node, so the sum is 0
            l_val = dfs(node.left)  # Maximum chain sum in the left subtree
            r_val = dfs(node.right)  # Maximum chain sum in the right subtree
            nonlocal ans
            ans = max(ans, l_val + r_val + node.val)  # Join the two chains into a path
            return max(max(l_val, r_val) + node.val, 0)  # Maximum chain sum in the current subtree
        dfs(root)
        return ans
