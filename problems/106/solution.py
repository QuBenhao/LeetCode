import solution
from typing import *
from object_libs import tree_to_list


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        inorder, postorder = test_input
        res = self.buildTree(inorder, postorder)
        return tree_to_list(res)

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return
        root_val = postorder[-1]
        idx = inorder.index(root_val)
        return TreeNode(root_val,
                        self.buildTree(inorder[:idx], postorder[:idx]),
                        self.buildTree(inorder[idx+1:], postorder[idx:len(postorder) - 1]))
