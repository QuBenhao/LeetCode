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
            if lock == '1':  # 不能改
                d = 1 if b == '(' else -1
                mx += d
                if mx < 0:  # c 不能为负
                    return False
                mn += d
            else:  # 可以改
                mx += 1  # 改成左括号，c 加一
                mn -= 1  # 改成右括号，c 减一
            if mn < 0:  # c 不能为负
                mn = 1  # 此时 c 的取值范围都是奇数，最小的奇数是 1
        return mn == 0  # 说明最终 c 能是 0
