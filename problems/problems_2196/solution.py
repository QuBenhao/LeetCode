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
        descriptions = test_input
        res = self.createBinaryTree(descriptions)
        return tree_to_list(res)

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        pass

