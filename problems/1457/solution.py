import solution
from python.object_libs import list_to_tree


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root = list_to_tree(test_input)
        return self.pseudoPalindromicPaths(root)

    def pseudoPalindromicPaths(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0

        def count_traversal(node, vals):
            if node.val in vals:
                vals.remove(node.val)
            else:
                vals.append(node.val)

            if not node.left and not node.right:
                if len(vals) < 2:
                    self.count += 1
                return
            if node.left:
                count_traversal(node.left, list(vals))
            if node.right:
                count_traversal(node.right, list(vals))

        count_traversal(root, [])
        return self.count


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
