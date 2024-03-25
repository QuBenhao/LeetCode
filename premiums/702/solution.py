import solution
from typing import *


# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.search(*test_input)

    def search(self, reader: 'ArrayReader', target: int) -> int:
            pass
        