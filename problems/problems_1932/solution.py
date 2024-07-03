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
        nums_arr = test_input
        roots = [list_to_tree(nums) for nums in nums_arr]
        res = self.canMerge(roots)
        return tree_to_list(res)

    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        pass

