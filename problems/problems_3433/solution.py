import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countMentions(*test_input)

    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        pass

