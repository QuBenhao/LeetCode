import solution
from typing import *



# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution(solution.Solution):
    def solve(self, test_input=None):
        node = test_input
        return self.inorderSuccessor(node)

    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
            pass
        