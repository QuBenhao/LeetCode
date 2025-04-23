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
        nums0 = test_input
        root0 = list_to_tree(nums0)
        return self.findBottomLeftValue(root0)

    def findBottomLeftValue(self, root: TreeNode) -> int:
        def dfs(node, level):
            if not node.left and not node.right:
                return node.val, level
            res, res_level = 0, 0
            if node.left:
                res, res_level = dfs(node.left, level + 1)
            if node.right:
                right, right_level = dfs(node.right, level + 1)
                if right_level > res_level:
                    res, res_level = right, right_level
            return res, res_level
        
        return dfs(root, 0)[0]
