import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getWinner(*test_input)

    def getWinner(self, arr: List[int], k: int) -> int:
        mx = arr[0]
        win = -1
        for x in arr:
            if x > mx:
                mx, win = x, 0
            win += 1
            if win == k:
                break
        return mx

