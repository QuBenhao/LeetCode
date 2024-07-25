import solution
from typing import *
from python.object_libs import list_to_tree_with_target, tree_to_list

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.

class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0, num1, num2 = test_input
        root, p, q = list_to_tree_with_target(nums0, num1, num2)
        res = self.lowestCommonAncestor(root, p, q)
        return tree_to_list(res)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
        return root
