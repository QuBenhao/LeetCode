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
        return self.longestUnivaluePath(root0)

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            if node is None:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            cur_ans, cur = 0, 0
            if node.left is not None and node.left.val == node.val:
                cur_ans = left + 1
                cur += left + 1
            if node.right is not None and node.right.val == node.val:
                cur_ans = max(cur_ans, right + 1)
                cur += right + 1
            nonlocal ans
            ans = max(ans, cur)
            return cur_ans

        dfs(root)
        return ans
