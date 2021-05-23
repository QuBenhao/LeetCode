import solution
import math


class Solution(solution.Solution):
    def solve(self, test_input=None):
        dist, hour = test_input
        return self.minSpeedOnTime(dist, hour)

    def minSpeedOnTime(self, dist, hour):
        """
        :type dist: List[int]
        :type hour: float
        :rtype: int
        """
        def helper(v):
            h = 0.0
            for d in dist[:-1]:
                t = float(d) / v
                h += math.ceil(t)
            h += float(dist[-1]) / v
            return h <= hour

        if hour <= len(dist) - 1:
            return -1
        l, r = 1, 10 ** 7
        while l < r:
            mid = (l + r) // 2
            if helper(mid):
                r = mid
            else:
                l = mid + 1
        return l