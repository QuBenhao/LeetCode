import solution
from typing import *
from python.object_libs import list_to_tree
from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0, targetSum = test_input
        root0 = list_to_tree(nums0)
        return self.pathSum(root0, targetSum)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node: Optional[TreeNode], counter: Counter[int], cur_sum: int) -> int:
            if not node:
                return 0
            cur_sum += node.val
            ans = counter[cur_sum - targetSum]
            counter[cur_sum] += 1
            if node.left:
                ans += dfs(node.left, counter, cur_sum)
            if node.right:
                ans += dfs(node.right, counter, cur_sum)
            counter[cur_sum] -= 1
            return ans

        return dfs(root, Counter({0: 1}), 0)

