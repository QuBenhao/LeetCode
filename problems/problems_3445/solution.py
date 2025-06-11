from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxDifference(*test_input)

    def maxDifference(self, s: str, k: int) -> int:
        """
        Find the max (prefix_sum[r+1][x] - prefix_sum[l][x]) - (prefix_sum[r+1][y] - prefix_sum[l][y])
        so when the r is fixed, we want to find the min prefix_sum[l][x] - prefix_sum[l][y]
        prefix_sum[r+1][x] must be greater than prefix_sum[l][x]
        and prefix_sum[r+1][y] must be greater than prefix_sum[l][y]
        prefix_sum[r+1][x] and prefix_sum[l][x] must have different parities
        where prefix_sum[l][x] and prefix_sum[l][y] must be the same parity
        """
        ans = -inf
        for x in range(5):
            for y in range(5):
                if x == y:
                    continue
                pre_sum = [0] * 5
                cur_sum = [0] * 5
                min_s = [[inf, inf], [inf, inf]]  # [even, odd]
                left = 0
                for i, c in enumerate(s):
                    cur_sum[ord(c) - ord('0')] += 1
                    while i - left + 1 >= k and cur_sum[x] > pre_sum[x] and cur_sum[y] > pre_sum[y]:
                        p, q = pre_sum[x] & 1, pre_sum[y] & 1
                        min_s[p][q] = min(min_s[p][q], pre_sum[x] - pre_sum[y])
                        pre_sum[ord(s[left]) - ord('0')] += 1
                        left += 1
                    if i + 1 >= k:
                        ans = max(ans, cur_sum[x] - cur_sum[y] - min_s[cur_sum[x] & 1 ^ 1][cur_sum[y] & 1])
        return ans
