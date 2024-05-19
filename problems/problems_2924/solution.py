import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findChampion(*test_input)

    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        count = [0] * n
        for a, b in edges:
            count[b] += 1
        ans = -1
        for i in range(n):
            if count[i] == 0:
                if ans != -1:
                    return -1
                ans = i
        return ans
