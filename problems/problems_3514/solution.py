import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.uniqueXorTriplets(test_input)

    def uniqueXorTriplets(self, nums: List[int]) -> int:
        d = set(nums)
        # step1: all x^y (includes x^x=0)
        t2 = {x ^ y for x in d for y in d}
        # step2: all (x^y)^z  ==  all a^b^c
        s = {t ^ z for t in t2 for z in d}
        return len(s)
