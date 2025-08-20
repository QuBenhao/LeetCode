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
        res = self.findDuplicateSubtrees(root0)
        return [tree_to_list(root) for root in res]

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        mp = dict()
        ans = dict()

        def dfs(node):
            if not node:
                return " "
            serial = f"{node.val},{dfs(node.left)},{dfs(node.right)}"
            if serial in mp and serial not in ans:
                ans[serial] = node
            mp[serial] = node
            return serial
        dfs(root)
        return list(ans.values())
