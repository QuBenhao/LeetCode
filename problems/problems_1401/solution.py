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
            Find the perpendicular projection of point p onto line AB.
            Return: (projection coordinates, t)
            If t is in [0,1], the projection lies on segment AB.
            """
            ax, ay = a
            bx, by = b
            px, py = p

            abx, aby = bx - ax, by - ay
            apx, apy = px - ax, py - ay

            ab2 = abx * abx + aby * aby

            # A and B coincide, so they do not define a line
            if ab2 == 0:
                return a, 0.0

            t = (apx * abx + apy * aby) / ab2
            foot = (ax + t * abx, ay + t * aby)

            return foot, t

        def foot_on_segment(p, a, b):
            """
            Find the closest point on segment AB to point p.
            If the perpendicular projection lies on the segment, use it;
            otherwise, return endpoint A or B.
            Return: (closest point coordinates, distance, t)
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
