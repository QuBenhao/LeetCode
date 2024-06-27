import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.partitionLabels(test_input)

    def partitionLabels(self, s: str) -> List[int]:
        idx_map = {c: i for i, c in enumerate(s)}
        ans = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, idx_map[c])
            if i == end:
                ans.append(end - start + 1)
                start = end + 1
        return ans
