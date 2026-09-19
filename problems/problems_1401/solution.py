from itertools import combinations
from math import hypot

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.checkOverlap(*test_input)

    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        def foot_on_line(p, a, b):
            """
            求点 p 到直线 AB 的垂足。
            返回: (垂足坐标, t)
            t 在 [0,1] 内表示垂足在线段 AB 上。
            """
            ax, ay = a
            bx, by = b
            px, py = p

            abx, aby = bx - ax, by - ay
            apx, apy = px - ax, py - ay

            ab2 = abx * abx + aby * aby

            # A、B 重合，无法确定直线
            if ab2 == 0:
                return a, 0.0

            t = (apx * abx + apy * aby) / ab2
            foot = (ax + t * abx, ay + t * aby)

            return foot, t

        def foot_on_segment(p, a, b):
            """
            求点 p 到线段 AB 的最近点。
            如果垂足在线段内，就是垂足；
            如果垂足在线段外，则返回端点 A 或 B。
            返回: (最近点坐标, 距离, t)
            """
            foot, t = foot_on_line(p, a, b)

            if t < 0:
                foot = a
                t = 0.0
            elif t > 1:
                foot = b
                t = 1.0

            dist = hypot(p[0] - foot[0], p[1] - foot[1])
            return foot, dist, t

        if min(x1, x2) <= xCenter <= max(x1, x2) and min(y1, y2) <= yCenter <= max(y1, y2):
            return True
        for p1 in [(x1, y1), (x2, y2)]:
            for p2 in [(x1, y2), (x2, y1)]:
                f, _, _ = foot_on_segment((xCenter, yCenter), p1, p2)
                x, y = f
                if (xCenter - x) ** 2 + (yCenter - y) ** 2 <= radius ** 2:
                    return True
        return False
