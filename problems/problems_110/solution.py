from typing import *

import solution
from python.object_libs import list_to_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0 = test_input
        root0 = list_to_tree(nums0)
        return self.isBalanced(root0)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(node) -> Tuple[int, bool]:
            if not node:
                return 0, True
            left, left_b = dfs(node.left)
            right, right_b = dfs(node.right)
            return max(left, right) + 1, left_b and right_b and abs(left - right) <= 1

        _, balanced = dfs(root)
        return balanced
