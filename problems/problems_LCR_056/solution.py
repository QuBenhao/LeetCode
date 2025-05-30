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
        nums0, k = test_input
        root0 = list_to_tree(nums0)
        return self.findTarget(root0, k)

    def findTarget(self, root: TreeNode, k: int) -> bool:
        pass

