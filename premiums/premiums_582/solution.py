import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.killProcess(*test_input)

    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
                pass