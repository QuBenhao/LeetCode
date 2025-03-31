from math import floor

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.percentageLetter(*test_input)

    def percentageLetter(self, s: str, letter: str) -> int:
        return floor(s.count(letter) * 100 / len(s))
