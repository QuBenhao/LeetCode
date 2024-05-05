import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.decrypt(*test_input)

    def decrypt(self, code: List[int], k: int) -> List[int]:
            pass