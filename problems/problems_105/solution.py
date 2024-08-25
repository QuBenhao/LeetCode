import solution
from typing import *
from python.object_libs import tree_to_list


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        preorder, inorder = test_input
        res = self.buildTree(preorder, inorder)
        return tree_to_list(res)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)
        root.left = self.buildTree(preorder[1:1 + root_index], inorder[:root_index])
        root.right = self.buildTree(preorder[1 + root_index:], inorder[root_index + 1:])
        return root
