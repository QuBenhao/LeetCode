import solution
from typing import *
from collections import defaultdict
from bisect import bisect_left


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.medianOfUniquenessArray(test_input)

    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        m = (n * (n + 1)) // 2
        k = (m + 1) // 2

        def check(upper: int) -> bool:
            count = l = 0
            freq = defaultdict(int)
            for r, num in enumerate(nums):
                freq[num] += 1
                while len(freq) > upper:
                    freq[nums[l]] -= 1
                    if not freq[nums[l]]:
                        del freq[nums[l]]
                    l += 1
                count += r - l + 1
            if count >= k:
                return True
            return False

        return bisect_left(range(len(set(nums))), True, 1, key=check)
