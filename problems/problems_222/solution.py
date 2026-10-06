import solution
from typing import *
from python.object_libs import list_to_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countNodes(list_to_tree(test_input))

    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        The depth of a perfect binary tree is found by recursively following left children.
        If the left and right subtree depths differ, the left subtree is not perfect and the right subtree is perfect. Recursively count the left subtree, then add the size of the perfect right subtree plus the root: (1 << right).
        If the left and right subtree depths are equal, the left subtree is perfect and the right subtree is not perfect. Recursively count the right subtree, then add the size of the perfect left subtree plus the root: (1 << left).
        """
        def depth(node):
            h = 0
            while node:
                node = node.left
                h += 1
            return h

        if not root:
            return 0
        left, right = depth(root.left), depth(root.right)
        if left == right:
            return self.countNodes(root.right) + (1 << left)
        else:
            return self.countNodes(root.left) + (1 << right)
