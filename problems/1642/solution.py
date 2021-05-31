import solution
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        heights, bricks, ladders = test_input
        return self.furthestBuilding(list(heights), bricks, ladders)

    def furthestBuilding(self, heights, bricks, ladders):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        pq = []
        n = len(heights)
        for i in range(n-1):
            if heights[i+1] <= heights[i]:
                continue
            diff = heights[i+1] - heights[i]
            heapq.heappush(pq, -diff)
            bricks -= diff
            if bricks < 0 and ladders:
                ladders -= 1
                bricks -= heapq.heappop(pq)
            elif bricks < 0:
                return i
        return n - 1
