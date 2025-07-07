import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.rotatedDigits(test_input)

    def rotatedDigits(self, n: int) -> int:
        return answers[n]


ROTATES = {'2', '5', '6', '9'}
answers = [0] * 10001
for i in range(1, 10001):
    s = str(i)
    if any(c in ROTATES for c in s) and not any(c in '347' for c in s):
        answers[i] = answers[i - 1] + 1
    else:
        answers[i] = answers[i - 1]