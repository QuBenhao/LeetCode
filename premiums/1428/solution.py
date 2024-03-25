import solution
from typing import *


# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.leftMostColumnWithOne(*test_input)

    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
            pass
        