import solution
from typing import *
from collections import defaultdict
from itertools import pairwise


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumSeconds(test_input)

    def minimumSeconds(self, nums: List[int]) -> int:
        idx_map = defaultdict(list)
        for i, num in enumerate(nums):
            idx_map[num].append(i)
        n = len(nums)
        ans = n
        for idxes in idx_map.values():
            idxes.append(idxes[0] + n)
            mx = max(b - a for a, b in pairwise(idxes))
            ans = min(ans, mx)
        return ans // 2
