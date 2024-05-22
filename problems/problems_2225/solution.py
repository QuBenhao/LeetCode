import solution
from typing import *
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findWinners(test_input)

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        div = defaultdict(int)
        for win, lose in matches:
            graph[win].append(lose)
            div[lose] += 1
        ans = [[], []]
        ans[0].extend(list(graph.keys() - div.keys()))
        ans[0].sort()
        for k, v in div.items():
            if v == 1:
                ans[1].append(k)
        ans[1].sort()
        return ans
