import solution
from typing import *
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.kSmallestPairs(*test_input)

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        pq, ans = [(nums1[0] + nums2[0], 0, 0)], []
        for _ in range(k):
            _, idx1, idx2 = heapq.heappop(pq)
            # 避免出现重复入堆
            if idx2 == 0 and idx1 < len(nums1) - 1:
                heapq.heappush(pq, (nums1[idx1 + 1] + nums2[idx2], idx1 + 1, idx2))
            if idx2 < len(nums2) - 1:
                heapq.heappush(pq, (nums1[idx1] + nums2[idx2 + 1], idx1, idx2 + 1))
            ans.append([nums1[idx1], nums2[idx2]])
        return ans
