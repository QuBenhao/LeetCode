from itertools import zip_longest

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minChanges(*test_input)

    def minChanges(self, n: int, k: int) -> int:
        return -1 if (n & k) != k else (n ^ k).bit_count()
