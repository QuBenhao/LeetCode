import solution
from typing import *


class Node(object):
    def __init__(self, val=" ", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
class Solution(solution.Solution):
    def solve(self, test_input=None):
        root1, root2 = test_input
        return self.checkEquivalence(root1, root2)

    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
            pass
        