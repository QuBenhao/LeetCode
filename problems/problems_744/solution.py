from bisect import bisect_right

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.nextGreatestLetter(*test_input)

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[idx] if (idx := bisect_right(letters, target)) < len(letters) else letters[0]
