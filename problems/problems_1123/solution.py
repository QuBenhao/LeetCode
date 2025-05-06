import solution
from typing import *
from python.object_libs import list_to_tree, tree_to_list


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0 = test_input
        root0 = list_to_tree(nums0)
        res = self.lcaDeepestLeaves(root0)
        return tree_to_list(res)

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> Tuple[Optional[TreeNode], int]:
            if not node:
                return node, 0
            left_node, left_depth = dfs(node.left)
            right_node, right_depth = dfs(node.right)
            if left_depth == right_depth:
                return node, left_depth + 1
            if left_depth < right_depth:
                return right_node, right_depth + 1
            return left_node, left_depth + 1
        
        return dfs(root)[0]
