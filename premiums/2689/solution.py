import solution
from typing import *


class RopeTreeNode(object):
    def __init__(self, len=0, val="", left=None, right=None):
        self.len = len
        self.val = val
        self.left = left
        self.right = right

# Definition for a rope tree node.
class Solution(solution.Solution):
    def solve(self, test_input=None):
        root, k = test_input
        return self.getKthCharacter(root, k)

    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """
        pass
        