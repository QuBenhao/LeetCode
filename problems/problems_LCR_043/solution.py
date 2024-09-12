from collections import deque
import solution
from typing import *
from python.object_libs import call_method, list_to_tree, tree_to_list
import python.object_libs.tree


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
        obj = CBTInserter(root0)
        return [None] + [tree_to_list(r) if isinstance((r := call_method(obj, op, *ipt)), python.object_libs.tree.TreeNode) else r for op, ipt in zip(ops[1:], inputs[1:])]


class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root
        self.binary = 0
        q = deque([root])
        while q:
            self.binary += 1
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def insert(self, v: int) -> int:
        self.binary += 1
        high = self.binary.bit_length() - 1
        node = self.root
        for i in range(high - 1, 0, -1):
            if (self.binary >> i) & 1:
                node = node.right
            else:
                node = node.left
        if self.binary & 1:
            node.right = TreeNode(v)
        else:
            node.left = TreeNode(v)
        return node.val

    def get_root(self) -> TreeNode:
        return self.root
