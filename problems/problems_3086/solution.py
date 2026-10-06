import solution
from typing import *
from itertools import accumulate
from math import inf

class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumMoves(*test_input)

    def minimumMoves(self, nums: List[int], k: int, max_changes: int) -> int:
        pos = []
        c = 0  # Length of consecutive ones in nums
        for i, x in enumerate(nums):
            if x == 0:
                continue
            pos.append(i)  # Record the positions of ones
            c = max(c, 1)
            if i > 0 and nums[i - 1] == 1:
                if i > 1 and nums[i - 2] == 1:
                    c = 3  # There are 3 consecutive ones
                else:
                    c = max(c, 2)  # There are 2 consecutive ones

        c = min(c, k)
        if max_changes >= k - c:
            # Each of the remaining k-c ones can be obtained in two operations
            return max(c - 1, 0) + (k - c) * 2

        n = len(pos)
        pre_sum = list(accumulate(pos, initial=0))

        ans = inf
        # max_changes ones can each be obtained in two operations; the rest must be moved to pos[i] one step at a time
        size = k - max_changes
        for right in range(size, n + 1):
            # s1+s2 is the sum of distances from every pos[j], for j in [left, right), to pos[(left+right)/2]
            left = right - size
            i = left + size // 2
            s1 = pos[i] * (i - left) - (pre_sum[i] - pre_sum[left])
            s2 = pre_sum[right] - pre_sum[i] - pos[i] * (right - i)
            ans = min(ans, s1 + s2)
        return ans + max_changes * 2
