import solution
from typing import *
from math import gcd


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countBeautifulPairs(test_input)

    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        counter = [0] * 10
        for num in nums:
            cur = num % 10
            for i, c in enumerate(counter):
                if c and gcd(cur, i) == 1:
                    ans += c
            while num >= 10:
                num //= 10
            counter[num] += 1
        return ans
