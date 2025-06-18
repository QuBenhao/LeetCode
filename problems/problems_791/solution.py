import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.customSortString(*test_input)

    def customSortString(self, order: str, s: str) -> str:
        counter = [0] * 26
        for c in s:
            counter[ord(c) - ord('a')] += 1
        result = []
        for c in order:
            if counter[ord(c) - ord('a')] > 0:
                result.append(c * counter[ord(c) - ord('a')])
                counter[ord(c) - ord('a')] = 0
        for i in range(26):
            if counter[i] > 0:
                result.append(chr(i + ord('a')) * counter[i])
        return ''.join(result)