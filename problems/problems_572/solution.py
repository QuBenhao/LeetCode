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
        nums0, nums1 = test_input
        root0 = list_to_tree(nums0)
        root1 = list_to_tree(nums1)
        return self.isSubtree(root0, root1)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        pass

