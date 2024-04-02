import solution
from typing import *
from object_libs import tree_to_list

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
class Solution(solution.Solution):
    def solve(self, test_input=None):
        inorder, postorder = test_input
        res = self.buildTree(inorder, postorder)
        return tree_to_list(res)

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
            pass