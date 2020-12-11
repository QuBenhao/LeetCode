import math

from itertools import combinations
import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestTriangleArea(test_input)

    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """

        def Area(x, y, z):
            xa, xb, xc = x[0], y[0], z[0]
            ya, yb, yc = x[1], y[1], z[1]

            xr, yr = xb - xa, yb - ya
            xs, ys = xc - xa, yc - ya

            return 0.500000 * abs(xr * ys - xs * yr)

        area = 0
        n = len(points)
        for i in range(n):
            x = points[i]
            for j in range(i + 1, n):
                y = points[j]
                for k in range(j + 1, n):
                    z = points[k]
                    if area < Area(x, y, z): area = Area(x, y, z)

        return area
