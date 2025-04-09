import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(*test_input)

    def minOperations(self, nums: List[int], k: int) -> int:
        ans, m = set(), nums[0]
        for num in nums:
            ans.add(num)
            m = min(m, num)
        if k > m:
            return -1
        return len(ans) - 1 if k in ans else len(ans)
