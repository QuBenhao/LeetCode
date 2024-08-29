import solution
from typing import *
from python.object_libs import call_method, list_to_tree


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Codec()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        pass

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        pass

