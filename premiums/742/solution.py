import solution
from typing import *
from object_libs import list_to_tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0, k = test_input
        root0 = list_to_tree(nums0)
        return self.findClosestLeaf(root0, k)

    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
            pass