from collections import defaultdict

from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxArea(test_input)

    def maxArea(self, coords: List[List[int]]) -> int:
        x_arr = [inf, inf, -inf, -inf] # min, sub_min, sub_max, max
        y_arr = [inf, inf, -inf, -inf]

        def update_m(x, y):
            def update(arr, _v):
                if _v < arr[0]:
                    arr[1] = arr[0]
                    arr[0] = _v
                elif _v < arr[1]:
                    arr[1] = _v
                if _v > arr[3]:
                    arr[2] = arr[3]
                    arr[3] = _v
                elif _v > arr[2]:
                    arr[2] = _v
            update(x_arr, x)
            update(y_arr, y)

        def find_max(arr, ne):
            return arr[-1] if arr[-1] != ne else arr[-2]

        def find_min(arr, ne):
            return arr[0] if arr[0] != ne else arr[1]

        x_axis = defaultdict(lambda: [inf, -inf])
        y_axis = defaultdict(lambda: [inf, -inf])

        for x, y in coords:
            update_m(x, y)
            x_axis[y][0] = min(x_axis[y][0], x)
            x_axis[y][1] = max(x_axis[y][1], x)
            y_axis[x][0] = min(y_axis[x][0], y)
            y_axis[x][1] = max(y_axis[x][1], y)

        ans = 0
        for y, (x1, x2) in x_axis.items():
            if x1 == x2:
                continue
            mn, mx = find_min(y_arr, y), find_max(y_arr, y)
            if mn != inf:
                ans = max(ans, (x2 - x1) * abs(mn - y))
            if mx != -inf:
                ans = max(ans, (x2 - x1) * abs(mx - y))

        for x, (y1, y2) in y_axis.items():
            if y1 == y2:
                continue
            mn, mx = find_min(x_arr, x), find_max(x_arr, x)
            if mn != inf:
                ans = max(ans, (y2 - y1) * abs(mn - x))
            if mx != -inf:
                ans = max(ans, (y2 - y1) * abs(mx - x))

        return ans if ans > 0 else -1
