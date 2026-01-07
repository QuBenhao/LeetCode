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
        return self.maxProduct(root0)

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        vals = set()
        def dfs(node):
            if node is None:
                return 0
            ans = node.val
            ans += dfs(node.left)
            ans += dfs(node.right)
            vals.add(ans)
            return ans

        res = 0
        total_sum = dfs(root)
        for val in vals:
            res = max(res, val * (total_sum - val))
        return res % MOD

MOD = 10**9 + 7
