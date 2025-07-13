import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.matchPlayersAndTrainers(*test_input)

    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        ans = 0
        i = 0
        for train in trainers:
            if players[i] <= train:
                ans += 1
                i += 1
                if i == len(players):
                    break
        return ans
