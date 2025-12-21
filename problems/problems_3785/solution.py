import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSwaps(*test_input)

    def minSwaps(self, nums: List[int], forbidden: List[int]) -> int:
        n = len(nums)
        counts = Counter(nums)
        counts_fb = Counter(forbidden)
        for k, v in counts_fb.items():
            if counts[k] + v > n:
                return -1
        final_counts = Counter()
        cnt = 0
        for num, fb in zip(nums, forbidden):
            if num == fb:
                final_counts[num] += 1
                cnt += 1
        return max((cnt + 1) // 2, max(final_counts.values()) if final_counts else 0)
