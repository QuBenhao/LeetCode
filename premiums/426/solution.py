import solution
from typing import *



# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(solution.Solution):
    def solve(self, test_input=None):
        root = test_input
        return self.treeToDoublyList(root)

    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
            pass
        