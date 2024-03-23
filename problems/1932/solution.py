import solution
from collections import deque, defaultdict
from object_libs import list_to_tree, tree_to_list


class Solution(solution.Solution):
    def solve(self, test_input=None):
        trees = [list_to_tree(nums) for nums in test_input]
        root = self.canMerge(trees)
        return tree_to_list(root)

    def canMerge(self, trees):
        """
        :type trees: List[TreeNode]
        :rtype: TreeNode
        """


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
