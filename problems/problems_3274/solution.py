import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkTwoChessboards(*test_input)

    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        return (ord(coordinate1[0]) + ord(coordinate1[1])) % 2 == (ord(coordinate2[0]) + ord(coordinate2[1])) % 2
