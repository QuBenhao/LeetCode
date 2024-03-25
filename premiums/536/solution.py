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
        s = test_input
        res = self.str2tree(s)
        return tree_to_list(res)

    def str2tree(self, s: str) -> Optional[TreeNode]:
            pass