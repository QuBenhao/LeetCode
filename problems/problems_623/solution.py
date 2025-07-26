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
        nums0, val, depth = test_input
        root0 = list_to_tree(nums0)
        res = self.addOneRow(root0, val, depth)
        return tree_to_list(res)

    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)

        def dfs(node: Optional[TreeNode], cur_d: int):
            if not node:
                return
            if cur_d == depth - 1:
                node.left = TreeNode(val, node.left)
                node.right = TreeNode(val, None, node.right)
            else:
                dfs(node.left, cur_d + 1)
                dfs(node.right, cur_d + 1)

        dfs(root, 1)
        return root
