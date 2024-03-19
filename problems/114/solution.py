import solution
from typing import *

from object_libs.tree import list_to_tree, tree_to_list


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        t = list_to_tree(test_input)
        self.flatten(t)
        return tree_to_list(t)

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        right = root.right
        self.flatten(root.left)
        self.flatten(root.right)
        root.left, root.right = None, root.left
        node = root
        while node.right:
            node = node.right
        node.right = right
