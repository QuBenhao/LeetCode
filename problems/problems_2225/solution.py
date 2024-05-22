import solution
from typing import *
from collections import Counter


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findWinners(test_input)

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        cnts = Counter()
        for win, lose in matches:
            cnts[win], cnts[lose] = cnts[win], cnts[lose] + 1
        ans = [[], []]
        for k, v in cnts.items():
            if v == 0:
                ans[0].append(k)
            elif v == 1:
                ans[1].append(k)
        ans[0].sort()
        ans[1].sort()
        return ans
