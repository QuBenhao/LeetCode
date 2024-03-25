import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Leaderboard()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class Leaderboard:

    def __init__(self):
        pass


    def addScore(self, playerId: int, score: int) -> None:
            pass


    def top(self, K: int) -> int:
            pass


    def reset(self, playerId: int) -> None:
            pass



# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)