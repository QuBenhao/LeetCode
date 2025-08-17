from functools import cache
from itertools import combinations

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.judgePoint24(test_input)

    def judgePoint24(self, cards: List[int]) -> bool:
        TARGET = 24
        EPLSION = 1e-6

        def backtrack(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - TARGET) < EPLSION

            for i, j in combinations(range(len(nums)), 2):
                x, y = nums[i], nums[j]
                next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                for op in ('+', '-', '*', '/', '--', '//'):
                    if op == '+':
                        next_nums.append(x + y)
                    elif op == '-':
                        next_nums.append(x - y)
                    elif op == '*':
                        next_nums.append(x * y)
                    elif op == '/':
                        if abs(y) < EPLSION:
                            continue
                        next_nums.append(x / y)
                    elif op == '--':
                        next_nums.append(y - x)
                    elif op == '//':
                        if abs(x) < EPLSION:
                            continue
                        next_nums.append(y / x)

                    if backtrack(next_nums):
                        return True
                    next_nums.pop()

            return False

        return backtrack([float(card) for card in cards])
