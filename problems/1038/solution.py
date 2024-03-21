import solution
from object_libs import list_to_tree, tree_to_list


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root = list_to_tree(test_input)
        return tree_to_list(self.bstToGst(root))

    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def inorder(node, s):
            if not node:
                return s
            s = inorder(node.right, s)
            s += node.val
            node.val = s
            return inorder(node.left, s)

        inorder(root, 0)
        return root


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
