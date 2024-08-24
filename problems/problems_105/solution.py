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
        pass

