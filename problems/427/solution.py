import solution
from typing import *



# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution(solution.Solution):
    def solve(self, test_input=None):
        grid = test_input
        return self.construct(grid)

    def construct(self, grid: List[List[int]]) -> 'Node':
            pass
        