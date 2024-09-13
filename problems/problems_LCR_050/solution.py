import solution
from typing import *
from python.object_libs import list_to_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0, targetSum = test_input
        root0 = list_to_tree(nums0)
        return self.pathSum(root0, targetSum)

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        pass

