import solution
from object_libs import list_to_tree


class Solution(solution.Solution):

    def solve(self, test_input=None):
        return self.minDiffInBST(list_to_tree(test_input))

    pre = -float('inf')
    res = float('inf')

    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return

        self.minDiffInBST(root.left)
        # evaluate and set the current node as the node previously evaluated
        self.res = min(self.res, root.val - self.pre)
        self.pre = root.val

        self.minDiffInBST(root.right)
        return self.res

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def setL(self, left):
        self.left = left

    def setR(self, right):
        self.right = right
