import solution
import heapq
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSumSquareDiff(*test_input)

    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        d = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2
        if sum(d) <= k:
            return 0
        d.sort(reverse=True)
        lo, hi = 0, d[0]
        while lo < hi:                          # 最小 x: 压平代价 <= k
            mid = (lo + hi) // 2
            if sum(v - mid for v in d if v > mid) <= k:
                hi = mid
            else:
                lo = mid + 1
        x = lo
        ans = cnt = 0
        for v in d:
            if v > x:
                k -= v - x; cnt += 1
            else:
                ans += v * v
        return ans + k * (x - 1) ** 2 + (cnt - k) * x * x
