import heapq
import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.kSmallestPairs(*test_input)

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        # To avoid duplicate heap entries, initially pair every element of nums1 with nums2[0]
        pq = [(nums1[i] + nums2[0], i, 0) for i in range(n1)]
        ans = []
        idx = 0
        while pq and idx < k:
            _, i, j = heapq.heappop(pq)
            ans.append([nums1[i], nums2[j]])
            if j + 1 < n2:
                heapq.heappush(pq, (nums1[i] + nums2[j + 1], i, j + 1))
            idx += 1
        return ans
