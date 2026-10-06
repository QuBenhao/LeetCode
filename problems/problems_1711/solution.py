import solution
from collections import Counter
from typing import *


class Solution(solution.Solution):
    # powersOfTwo = [2 ** i for i in range(22)]
    # mod = 10 ** 9 + 7

    def solve(self, test_input=None):
        return self.countPairs(list(test_input))

    def countPairs(self, deliciousness: List[int]) -> int:
        """
        :type deliciousness: List[int]
        :rtype: int
        """
        # cnts = Counter(deliciousness)
        # return (sum(
        #     cnts[key] * (cnts[key] - 1) if key == target - key else cnts[key] * cnts[target - key]
        #     for key in cnts for target in self.powersOfTwo)) // 2 % self.mod

        MOD = 1000000007
        count = Counter(deliciousness)

        res = 0
        # Each number considers only pairs summing to its next power of two, avoiding duplicates: 1+3=4 is counted only at 3, and 3+5=8 only at 5
        for i in count:
            if i == 0:
                continue
            # The next power of two after i
            target = self.nextPower(i)
            # If i can combine with a key in count to reach this power
            res += count[i] * count[target - i]
            # If i itself is a power of two
            if i == target:
                res += count[i] * (count[i] - 1) // 2
        return res % MOD

    def nextPower(self, x: int):
        x -= 1
        x |= x >> 1
        x |= x >> 2
        x |= x >> 4
        x |= x >> 8
        x |= x >> 16
        return x + 1
