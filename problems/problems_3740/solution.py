from collections import defaultdict
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumDistance(test_input)

    def minimumDistance(self, nums: List[int]) -> int:
        ans = inf
        record = defaultdict(list)
        for k, num in enumerate(nums):
            record[num].append(k)
            if len(record[num]) > 2:
                i = record[num][-3]
                ans = min(ans, (k - i) * 2)
        return ans if ans != inf else -1
