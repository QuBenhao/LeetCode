import solution
from typing import *
from object_libs import list_to_tree, tree_to_list


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        root = list_to_tree(test_input)
        bst = self.balanceBST(root)
        return tree_to_list(bst)

    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        nodes = []

        def in_order(node):
            if not node:
                return
            in_order(node.left)
            nodes.append(node)
            in_order(node.right)

        in_order(root)

        def construct_AVL(nodes):
            if not nodes:
                return
            mid = len(nodes) // 2
            node = nodes[mid]
            node.left = construct_AVL(nodes[:mid])
            node.right = construct_AVL(nodes[mid+1:])
            return node

        return construct_AVL(nodes)
