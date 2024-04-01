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
        n = test_input
        res = self.allPossibleFBT(n)
        return tree_to_list(res)

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
            pass