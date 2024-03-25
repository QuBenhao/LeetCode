import solution
from typing import *
from object_libs import list_to_tree


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countNodes(list_to_tree(test_input))

    def countNodes(self, root: Optional[TreeNode]) -> int:
        """
        满二叉树的深度由它一直往左递归构成。
        如果左右子树深度不一致，说明左子树是不满的，右子树是满的，我们递归统计左子树，加上当前右子树的满二叉树数目 + 根节点 (1 << right)
        如果左右子树深度一致，说明左子树是满的，右子树是不满的，我们递归统计右子树，加上当前左子树的满二叉树数目 + 根节点 (1 << left)
        """
        def depth(node):
            h = 0
            while node:
                node = node.left
                h += 1
            return h

        if not root:
            return 0
        left, right = depth(root.left), depth(root.right)
        if left == right:
            return self.countNodes(root.right) + (1 << left)
        else:
            return self.countNodes(root.left) + (1 << right)
