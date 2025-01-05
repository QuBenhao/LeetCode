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
        self.banknotes = [0] * 5
        self.amounts = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i, count in enumerate(banknotesCount):
            self.banknotes[i] += count

    def withdraw(self, amount: int) -> List[int]:
        res = [0] * 5
        for i in range(4, -1, -1):
            res[i] = min(self.banknotes[i], amount // self.amounts[i])
            amount -= res[i] * self.amounts[i]
        if amount:
            return [-1]
        for i in range(5):
            self.banknotes[i] -= res[i]
        return res
