import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        x, y, points = test_input
        return self.nearestValidPoint(x, y, [k[:] for k in points])

    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        ans, dis = -1, float("inf")
        for i in range(len(points)):
            x1, y1 = points[i]
            if x1 == x or y1 == y:
                d = abs(x - x1) + abs(y - y1)
                if d < dis:
                    dis = d
                    ans = i
        return ans
