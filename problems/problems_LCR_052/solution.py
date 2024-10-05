import solution
from typing import *
from python.object_libs import list_to_tree, tree_to_list


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0 = test_input
        root0 = list_to_tree(nums0)
        res = self.increasingBST(root0)
        return tree_to_list(res)

    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.cur.right = TreeNode(node.val)
            self.cur = self.cur.right
            inorder(node.right)

        dummy = self.cur = TreeNode()
        inorder(root)
        return dummy.right
