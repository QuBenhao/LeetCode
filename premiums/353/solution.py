import solution
from typing import *
from object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = SnakeGame(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
            pass
        

    def move(self, direction: str) -> int:
            pass
        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)