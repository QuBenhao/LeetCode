from bisect import bisect_left

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.longestSubsequence(test_input)

    def longestSubsequence(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            st = []
            for num in nums:
                if (num >> i) & 1:
                    idx = bisect_left(st, num)
                    if idx == len(st):
                        st.append(num)
                    else:
                        st[idx] = num
            ans = max(ans, len(st))
        return ans
