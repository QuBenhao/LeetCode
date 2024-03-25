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
        s = test_input
        return self.expTree(s)

    def expTree(self, s: str) -> 'Node':
            pass
        