import solution
from typing import *
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallestRange(test_input)

    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        max_num = -10**5
        min_range = 10**5
        heap = [(nums[i][0], i, 0) for i in range(n)]
        heapq.heapify(heap)
        for i in range(n):
            max_num = max(max_num, nums[i][0])
        ans = [heap[0][0], max_num]
        while heap:
            min_num, i, j = heapq.heappop(heap)
            if max_num - min_num < min_range:
                min_range = max_num - min_num
                ans = [min_num, max_num]
            if j == len(nums[i]) - 1:
                return ans
            max_num = max(max_num, nums[i][j + 1])
            heapq.heappush(heap, (nums[i][j + 1], i, j + 1))
        return ans
