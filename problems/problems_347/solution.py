import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.topKFrequent(*test_input)


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        pq = []
        counter = Counter(nums)
        for key, val in counter.items():
            heapq.heappush(pq, (val, key))
            if len(pq) > k:
                heapq.heappop(pq)
        return [num for _, num in pq]

