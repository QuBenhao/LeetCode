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
        nums0, nums_arr = test_input
        root0 = list_to_tree(nums0)
        roots = [list_to_tree(nums) for nums in nums_arr]
        res = self.lowestCommonAncestor(root0, roots)
        return tree_to_list(res)

    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
            pass
        