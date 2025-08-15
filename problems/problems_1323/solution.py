import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximum69Number(test_input)

    def maximum69Number (self, num: int) -> int:
        return int(s.replace('6', '9', 1)) if '6' in (s := str(num)) else num

