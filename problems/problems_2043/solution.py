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
        self.balance = balance

    def check_account(self, account: int, money: int = None) -> bool:
        if account > len(self.balance) or account <= 0:
            return False
        if money is None:
            return True
        return money <= self.balance[account - 1]

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.check_account(account1, money) and self.check_account(account2):
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if self.check_account(account):
            self.balance[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if self.check_account(account, money):
            self.balance[account - 1] -= money
            return True
        return False
