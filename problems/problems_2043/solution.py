import solution
from typing import *
from python.object_libs import call_method


class Solution(solution.Solution):
    def solve(self, test_input=None):
        ops, inputs = test_input
        obj = Bank(*inputs[0])
        return [None] + [call_method(obj, op, *ipt) for op, ipt in zip(ops[1:], inputs[1:])]


class Bank:
    def __init__(self, balance: List[int]):
        pass

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        pass

    def deposit(self, account: int, money: int) -> bool:
        pass

    def withdraw(self, account: int, money: int) -> bool:
        pass

