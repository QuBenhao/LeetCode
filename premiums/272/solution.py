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
        nums0, target, k = test_input
        root0 = list_to_tree(nums0)
        return self.closestKValues(root0, target, k)

    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
                pass