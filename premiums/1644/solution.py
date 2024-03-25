import solution
from typing import *
from object_libs import list_to_tree, tree_to_list

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.

class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0, nums1, nums2 = test_input
        root0 = list_to_tree(nums0)
        root1 = list_to_tree(nums1)
        root2 = list_to_tree(nums2)
        res = self.lowestCommonAncestor(root0, root1, root2)
        return tree_to_list(res)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
                pass
        