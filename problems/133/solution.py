import solution
from typing import *


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(solution.Solution):
    def solve(self, test_input=None):
        pass

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        