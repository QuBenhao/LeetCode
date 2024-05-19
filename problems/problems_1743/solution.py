import solution
from typing import *
from collections import defaultdict


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.restoreArray(test_input)

    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        connect = defaultdict(set)
        for a, b in adjacentPairs:
            connect[a].add(b)
            connect[b].add(a)
        point = min(connect.keys(), key=lambda x: (len(connect[x]), x))
        explored = {point}
        ans = [point]
        while len(ans) < len(connect.keys()):
            point = (connect[point] - explored).pop()
            explored.add(point)
            ans.append(point)
        return ans
