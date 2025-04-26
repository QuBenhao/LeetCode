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
        res = self.convertBST(root0)
        return tree_to_list(res)

    def convertBST(self, root: TreeNode) -> TreeNode:
        cur_sum = 0
        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.right)
            nonlocal cur_sum
            cur_sum += node.val
            node.val = cur_sum
            dfs(node.left)

        dfs(root)
        return root
