import solution
from typing import *
from python.object_libs import list_to_tree
from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0 = test_input
        root0 = list_to_tree(nums0)
        return self.minDepth(root0)

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        ans = inf
        if root.left:
            ans = self.minDepth(root.left) + 1
        if root.right:
            ans = min(ans, self.minDepth(root.right) + 1)
        return ans
