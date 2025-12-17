import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.swapNumbers(test_input)

    def swapNumbers(self, numbers: List[int]) -> List[int]:
        numbers[0] ^= numbers[1]
        numbers[1] ^= numbers[0]
        numbers[0] ^= numbers[1]
        return numbers
