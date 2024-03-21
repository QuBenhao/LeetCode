import solution
from object_libs import list_to_tree


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root_nums,low,high = test_input
        root = list_to_tree(root_nums)
        return self.rangeSumBST(root,low,high)

    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if not root:
            return 0
        if low <= root.val <= high:
            return self.rangeSumBST(root.left,low,root.val) + self.rangeSumBST(root.right,root.val,high) + root.val
        elif root.val > high:
            return self.rangeSumBST(root.left,low,high)
        else:
            return self.rangeSumBST(root.right,low,high)


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def setL(self, left):
        self.left = left

    def setR(self, right):
        self.right = right
