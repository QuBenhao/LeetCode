import solution
from typing import *
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumLength(test_input)

    def maximumLength(self, s: str) -> int:
        group_counts = defaultdict(list)
        count = 0
        for i, c in enumerate(s):
            count += 1
            if i == len(s) - 1 or c != s[i + 1]:
                group_counts[c].append(count)
                count = 0
        ans = 0
        for counts in group_counts.values():
            counts.sort(reverse=True)
            counts.extend([0, 0])
            ans = max(ans, counts[0] - 2, min(counts[0] - 1, counts[1]), counts[2])
        return ans if ans else -1

