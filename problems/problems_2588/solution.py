from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.beautifulSubarrays(test_input)

    def beautifulSubarrays(self, nums: List[int]) -> int:
        ans = s = 0
        cnt = defaultdict(int)
        cnt[0] = 1
        for x in nums:
            s ^= x
            ans += cnt[s]
            cnt[s] += 1
        return ans
