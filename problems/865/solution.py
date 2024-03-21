import solution
from object_libs import list_to_tree, tree_to_list


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root = list_to_tree(test_input)
        node = self.subtreeWithAllDeepest(root)
        return tree_to_list(node)

    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        def search(node):
            if not node:
                return None, 0
            l_node, l_depth = search(node.left)
            r_node, r_depth = search(node.right)

            if l_depth == r_depth:
                return node, l_depth + 1
            elif l_depth < r_depth:
                return r_node, r_depth + 1
            else:
                return l_node, l_depth + 1

        node, _ = search(root)

        return node


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
