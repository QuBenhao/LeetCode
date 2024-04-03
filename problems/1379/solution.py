from collections import deque

import solution
from typing import *
from object_libs import list_to_tree_with_target, list_to_tree, tree_to_list


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0, target_val = test_input
        root0, target = list_to_tree_with_target(nums0, target_val)
        cloned = list_to_tree(nums0)
        res = self.getTargetCopy(root0, cloned, target)
        return res.val

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = deque([(original, cloned)])
        while q:
            o, c = q.popleft()
            if o == target:
                return c
            if o.left:
                q.append((o.left, c.left))
            if o.right:
                q.append((o.right, c.right))
