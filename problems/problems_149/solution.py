import solution
from collections import Counter
from math import inf


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxPoints([x[:] for x in test_input])

    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # # 三点在一条直线上时,斜率相等
        # # y2 - y1 = k * (x2 - x1), y3 - y2 = k * (x3 - x2)
        # # (y2 - y1) * (x3 - x2) = (y3 - y2) * (x2 - x1)
        # explored = set()
        # ans = 1
        # for i in range(len(points)):
        #     for j in range(i + 1, len(points)):
        #         curr = 2
        #         dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
        #         for k in range(j + 1, len(points)):
        #             if (i, j) in explored or (i, k) in explored or (j, k) in explored:
        #                 continue
        #             if dy * (points[k][0] - points[j][0]) == (points[k][1] - points[j][1]) * dx:
        #                 curr += 1
        #                 explored.add((j, k))
        #                 explored.add((i, k))
        #         ans = max(ans, curr)
        # return ans

        ans = 1
        for i in range(len(points) - 1):
            curr = Counter()
            for j in range(i + 1, len(points)):
                dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
                curr[dy / dx if dx else inf] += 1
            ans = max(ans, max(curr.values()) + 1)
        return ans
