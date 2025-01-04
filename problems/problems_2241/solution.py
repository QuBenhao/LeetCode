import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = ATM()
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class ATM:
    def __init__(self):
        pass

    def deposit(self, banknotesCount: List[int]) -> None:
        pass

    def withdraw(self, amount: int) -> List[int]:
        pass

