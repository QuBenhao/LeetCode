import solution
from typing import *
from object_libs import list_to_tree


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
        return self.maxAncestorDiff(root0)

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(node, mx, mn):
            if not node:
                return 0
            cur = max(mx - node.val, node.val - mn)
            mx, mn = max(node.val, mx), min(node.val, mn)
            left, right = helper(node.left, mx, mn), helper(node.right, mx, mn)
            return max(cur, left, right)

        return helper(root, root.val, root.val)
