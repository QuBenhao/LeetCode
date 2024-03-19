import solution
from object_libs import list_to_tree


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root = list_to_tree(test_input)
        return self.isBalanced(root)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def depth(node, d):
            if not node:
                return d, True
            d += 1
            l, l_t = depth(node.left, d)
            if not l_t:
                return None, False
            r, r_t = depth(node.right, d)
            if not r_t:
                return None, False
            return max(l, r), abs(l - r) <= 1

        _, res = depth(root, 0)
        return res


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
