import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.asteroidCollision(test_input)

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while stack and stack[-1] > 0 > a:
                if -a == stack[-1]:
                    stack.pop()
                    break
                elif stack[-1] < -a:
                    stack.pop()
                    continue
                else:
                    break
            else:
                stack.append(a)
        return stack
