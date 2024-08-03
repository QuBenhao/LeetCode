import solution
from python.object_libs import list_to_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root = list_to_tree(test_input)
        return self.isValidBST(root)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def valid(root, minv, maxv):
            if not root:
                return True
            if minv is not None:
                if root.val <= minv:
                    return False
            if maxv is not None:
                if root.val >= maxv:
                    return False
            return valid(root.left, minv, root.val) and valid(root.right, root.val, maxv)

        return valid(root, None, None)
