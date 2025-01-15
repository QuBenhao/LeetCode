import solution
from typing import *
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minOperations(*test_input)

    def minOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        heapq.heapify(nums)
        while len(nums) >= 2:
            first = heapq.heappop(nums)
            if first >= k:
                break
            second = heapq.heappop(nums)
            heapq.heappush(nums, first * 2 + second)
            ans += 1
        return ans
