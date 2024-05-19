import solution
from typing import *


class InfiniteStream:
    def next(self) -> int:
        pass

# Definition for an infinite stream.
class Solution(solution.Solution):
    def solve(self, test_input=None):
        stream, pattern = test_input
        return self.findPattern(stream, pattern)

    def findPattern(self, stream: Optional['InfiniteStream'], pattern: List[int]) -> int:
            pass
        