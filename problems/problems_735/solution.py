import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.asteroidCollision(test_input)

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            if a > 0:
                ans.append(a)
            else:
                while ans and 0 < ans[-1] < -a:
                    ans.pop()
                if not ans or ans[-1] < 0:
                    ans.append(a)
                elif ans[-1] == -a:
                    ans.pop()
        return ans
