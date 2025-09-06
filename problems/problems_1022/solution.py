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
        return self.sumRootToLeaf(root0)

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def dfs(node: TreeNode, cur: int) -> int:
            cur <<= 1
            cur += node.val
            if not node.left and not node.right:
                return cur
            ans = 0
            if node.left:
                ans += dfs(node.left, cur)
            if node.right:
                ans += dfs(node.right, cur)
            return ans

        return dfs(root, 0)
