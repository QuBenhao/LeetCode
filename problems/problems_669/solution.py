import solution
from python.object_libs import list_to_tree, tree_to_list


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums, low, high = test_input
        root = list_to_tree(nums)
        root = self.trimBST(root, low, high)
        return tree_to_list(root)

    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if not root:
            return
        if low <= root.val <= high:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        elif root.val > high:
            root = self.trimBST(root.left, low, high)
        else:
            root = self.trimBST(root.right, low, high)
        return root


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
