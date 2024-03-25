import solution
from typing import *



# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution(solution.Solution):
    def solve(self, test_input=None):
        root = test_input
        return self.diameter(root)

    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        pass