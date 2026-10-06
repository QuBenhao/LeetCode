import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.canReachCorner(*test_input)

    def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
        # Check whether point (x,y) is inside circle (ox,oy,r)
        def in_circle(ox: int, oy: int, r: int, x: int, y: int) -> bool:
            return (ox - x) * (ox - x) + (oy - y) * (oy - y) <= r * r

        vis = [False] * len(circles)

        def dfs(i: int) -> bool:
            x1, y1, r1 = circles[i]
            # Whether circle i intersects or touches the rectangle's right or bottom boundary
            if y1 <= Y and abs(x1 - X) <= r1 or \
                    x1 <= X and y1 <= r1 or \
                    x1 > X and in_circle(x1, y1, r1, X, 0):
                return True
            vis[i] = True
            for j, (x2, y2, r2) in enumerate(circles):
                # Given that the two circles intersect or touch, whether point A is strictly inside the rectangle
                if not vis[j] and \
                        (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) <= (r1 + r2) * (r1 + r2) and \
                        x1 * r2 + x2 * r1 < (r1 + r2) * X and \
                        y1 * r2 + y2 * r1 < (r1 + r2) * Y and \
                        dfs(j):
                    return True
            return False

        for i, (x, y, r) in enumerate(circles):
            # Circle i contains the rectangle's bottom-left corner, or
            # Circle i contains the rectangle's top-right corner, or
            # Circle i intersects or touches the rectangle's top or left boundary
            if in_circle(x, y, r, 0, 0) or \
                    in_circle(x, y, r, X, Y) or \
                    not vis[i] and (x <= X and abs(y - Y) <= r or
                                    y <= Y and x <= r or
                                    y > Y and in_circle(x, y, r, 0, Y)) and dfs(i):
                return False
        return True
