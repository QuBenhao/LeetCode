import solution
from typing import *
from python.object_libs import list_to_tree, tree_to_list


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0 = test_input
        root0 = list_to_tree(nums0)
        res = self.upsideDownBinaryTree(root0)
        return tree_to_list(res)

    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        node, left, right = None, root, None
        while left:
            new_left, new_right = left.left, left.right
            left.left = right
            left.right = node
            node, left, right = left, new_left, new_right
        return node
