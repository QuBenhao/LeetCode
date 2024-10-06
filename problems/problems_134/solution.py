import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canCompleteCircuit(*test_input)

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas) < sum(cost):
            return -1
        start = 0
        remain = 0
        for i in range(n):
            remain += gas[i] - cost[i]
            if remain < 0:
                start = i + 1
                remain = 0
        return start
