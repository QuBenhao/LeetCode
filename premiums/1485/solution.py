import solution
from typing import *


class Node:
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random

# Definition for Node.

class Solution(solution.Solution):
    def solve(self, test_input=None):
        root = test_input
        return self.copyRandomBinaryTree(root)

    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
            pass
        