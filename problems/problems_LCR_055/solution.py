import solution
from typing import *
from python.object_libs import call_method, list_to_tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        nums0 = inputs[0][0]
        root0 = list_to_tree(nums0)
        obj = BSTIterator(root0)
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        if not self.stack:
            return 0
        node = self.stack.pop()
        val = node.val
        node = node.right
        while node:
            self.stack.append(node)
            node = node.left
        return val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

