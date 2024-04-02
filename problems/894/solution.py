import solution
from typing import *
from object_libs import tree_to_list
import itertools


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
class Solution(solution.Solution):
    def solve(self, test_input=None):
        n = test_input
        res = self.allPossibleFBT(n)
        return [tree_to_list(root) for root in res]

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        ans = []
        if n % 2 != 0:
            if n == 1:
                ans.append(TreeNode())
            else:
                for i in range(1, n, 2):
                    a, b = self.allPossibleFBT(i), self.allPossibleFBT(n - 1 - i)
                    for l, r in itertools.product(a, b):
                        ans.append(TreeNode(left=l, right=r))
        return ans
