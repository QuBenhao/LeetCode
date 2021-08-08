import solution
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        piles, k = test_input
        return self.minStoneSum(list(piles), k)

    def minStoneSum(self, piles, k):
        """
        :type piles: List[int]
        :type k: int
        :rtype: int
        """
        pq = []
        for p in piles:
            heapq.heappush(pq, -p)
        for i in range(k):
            heapq.heappush(pq, heapq.heappop(pq) // 2)
        return -sum(pq)
