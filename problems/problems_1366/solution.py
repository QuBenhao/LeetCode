from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rankTeams(test_input)

    def rankTeams(self, votes: List[str]) -> str:
        m = len(votes[0])
        counter = defaultdict(lambda: [0] * m)
        for vote in votes:
            for i, ch in enumerate(vote):
                counter[ch][i] -= 1
        return ''.join(sorted(counter, key=lambda c: (counter[c], c)))
