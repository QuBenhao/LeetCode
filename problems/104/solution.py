import solution
from object_libs import list_to_tree


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root = list_to_tree(test_input)
        return self.maxDepth(root)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def depth(node, d):
            if not node:
                return d
            if not node.left and not node.right:
                return d + 1
            d += 1
            return max(depth(node.left, d), depth(node.right, d))

        return depth(root, 0)


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
