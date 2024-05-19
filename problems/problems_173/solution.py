import solution
from typing import Optional
from python.object_libs import list_to_tree, call_method


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(solution.Solution):
    def solve(self, test_input=None):
        operations, inputs = test_input
        root = list_to_tree(*inputs[0])
        obj = BSTIterator(root)
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(operations[1:], inputs[1:])]


class BSTIterator:
    """
    def __init__(self, root):
        self.root = root
        self.arr = []

        def in_order(node):
            if not node:
                return
            in_order(node.left)
            self.arr.append(node)
            in_order(node.right)

        in_order(root)
        self.curr = 0

    def next(self):
        val = self.arr[self.curr].val
        self.curr += 1
        return val

    def hasNext(self):
        return self.curr < len(self.arr)
    """

    def __init__(self, root: Optional[TreeNode]):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.in_order(root)

    def in_order(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node = self.stack.pop(-1)
        if node.right:
            self.in_order(node.right)

        return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return bool(self.stack)
