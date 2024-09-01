import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxConsecutiveAnswers(*test_input)

    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        l, r = 0, 0
        count = {'T': 0, 'F': 0}
        ans = 0
        while r < n:
            count[answerKey[r]] += 1
            r += 1
            while min(count['T'], count['F']) > k:
                count[answerKey[l]] -= 1
                l += 1
            ans = max(ans, r - l)
        return ans
