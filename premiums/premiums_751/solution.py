import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.ipToCIDR(*test_input)

    def ipToCIDR(self, ip: str, n: int) -> List[str]:
            pass