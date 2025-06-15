from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.specialTriplets(test_input)

    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        count = defaultdict(int)
        pre_count = defaultdict(int)
        ans = 0
        for num in nums:
            if num % 2 == 0:
                ans = (ans + count[(num, num//2)]) % MOD
            if pre_count[num*2]:
                count[(num*2,num)] += pre_count[num*2]
            pre_count[num] += 1
        return ans
