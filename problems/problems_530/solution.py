import solution
from python.object_libs import list_to_tree


class Solution(solution.Solution):

    def solve(self, test_input=None):
        return self.getMinimumDifference(list_to_tree(test_input))

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def in_order(prev, curr, m):
            if not curr:
                return prev, m
            prev, m = in_order(prev, curr.left, m)
            m, prev = min(m, curr.val - prev), curr.val
            return in_order(prev, curr.right, m)

        return in_order(-float("inf"),root,float("inf"))[1]


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
