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
        nums0, k = test_input
        root0 = list_to_tree(nums0)
        return self.kthSmallest(root0, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            if not node:
                return
            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)

        iterator, ans = inorder(root), -1
        for i in range(k):
            ans = next(iterator)
        return ans
