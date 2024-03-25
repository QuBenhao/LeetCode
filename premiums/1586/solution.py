import solution
from typing import *
from object_libs import call_method, list_to_tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(solution.Solution):
    def solve(self, test_input=None):
        nums0 = test_input
        root0 = list_to_tree(nums0)
        obj = BSTIterator(root0)
                return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

# Definition for a binary tree node.
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        pass


    def hasNext(self) -> bool:
        pass


    def next(self) -> int:
        pass


    def hasPrev(self) -> bool:
        pass


    def prev(self) -> int:
        pass



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()