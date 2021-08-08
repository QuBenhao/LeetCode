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
        piles = [-x for x in piles]
        heapq.heapify(piles)
        for i in range(k):
            x = heapq.heappop(piles)
            heapq.heappush(piles, x // 2)
        return -sum(piles)
