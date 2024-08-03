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
        ,  = test_input
        return self.isSubtree(, )

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        pass

