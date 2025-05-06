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
        pass

    def next(self) -> int:
        pass

    def hasNext(self) -> bool:
        pass

