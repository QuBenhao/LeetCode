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

    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        def dfs(node, counter, cur):
            if not node:
                return 0
            cur += node.val
            ans = counter[cur - targetSum]
            counter[cur] += 1
            ans += dfs(node.left, counter, cur)
            ans += dfs(node.right, counter, cur)
            counter[cur] -= 1
            return ans

        return dfs(root, Counter({0: 1}), 0)
