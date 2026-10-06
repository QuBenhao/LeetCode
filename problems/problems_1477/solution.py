from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSumOfLengths(*test_input)

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # pre[i] = length of the shortest subarray in arr[:i] with sum target (entirely to the left of i)
        pre = [inf] * (len(arr) + 1)
        last = {0: 0}  # Prefix sum -> most recent position; the latest position gives the shortest subarray
        s = 0
        ans = inf
        for i, v in enumerate(arr, 1):
            s += v
            pre[i] = pre[i - 1]
            if s - target in last:
                j = last[s - target]  # Right subarray arr[j:i]
                ans = min(ans, pre[j] + i - j)  # pre[j] is entirely to the left of j, so the subarrays do not overlap
                pre[i] = min(pre[i], i - j)
            last[s] = i
        return ans if ans != inf else -1
