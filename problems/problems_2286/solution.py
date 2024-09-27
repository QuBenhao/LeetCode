import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = BookMyShow(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class BookMyShow:
    def __init__(self, n: int, m: int):
        pass

    def gather(self, k: int, maxRow: int) -> List[int]:
        pass

    def scatter(self, k: int, maxRow: int) -> bool:
        pass

