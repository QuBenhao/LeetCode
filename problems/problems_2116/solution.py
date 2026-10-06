import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canBeValid(*test_input)

    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
        mn = mx = 0
        for b, lock in zip(s, locked):
            if lock == '1':  # Cannot be changed
                d = 1 if b == '(' else -1
                mx += d
                if mx < 0:  # c cannot be negative
                    return False
                mn += d
            else:  # Can be changed
                mx += 1  # Change to an opening parenthesis: increment c
                mn -= 1  # Change to a closing parenthesis: decrement c
            if mn < 0:  # c cannot be negative
                mn = 1  # All possible values of c are odd here; the smallest valid odd value is 1
        return mn == 0  # This means c can end at 0
