import solution
from typing import *
from object_libs import list_to_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0, nums1 = test_input
        root0 = list_to_tree(nums0)
        root1 = list_to_tree(nums1)
        return self.isSameTree(root0, root1)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return (not p and not q) or (p is not None and q is not None and p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right))
