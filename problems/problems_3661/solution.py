from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxWalls(*test_input)

    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        n, m = len(robots), len(walls)
        a = [(0, 0)] + sorted(zip(robots, distance), key=lambda p: p[0]) + [(inf, 0)]
        walls.sort()

        f0 = f1 = left = cur = right0 = right1 = 0
        for i in range(1, n + 1):
            x, d = a[i]

            # 往左射，墙的坐标范围为 [left_x, x]
            left_x = max(x - d, a[i - 1][0] + 1)  # +1 表示不能射到左边那个机器人
            while left < m and walls[left] < left_x:
                left += 1
            while cur < m and walls[cur] < x:
                cur += 1
            cur1 = cur
            if cur < m and walls[cur] == x:
                cur += 1
            left_res = f0 + cur - left  # 下标在 [left, cur-1] 中的墙都能摧毁

            # 往右射，右边那个机器人往左射，墙的坐标范围为 [x, right_x]
            x2, d2 = a[i + 1]
            right_x = min(x + d, x2 - d2 - 1)  # -1 表示不能射到右边那个机器人
            while right0 < m and walls[right0] <= right_x:
                right0 += 1
            f0 = max(left_res, f1 + right0 - cur1)  # 下标在 [cur1, right0-1] 中的墙都能摧毁

            # 往右射，右边那个机器人往右射，墙的坐标范围为 [x, right_x]
            right_x = min(x + d, x2 - 1)  # -1 表示不能射到右边那个机器人
            while right1 < m and walls[right1] <= right_x:
                right1 += 1
            f1 = max(left_res, f1 + right1 - cur1)  # 下标在 [cur1, right1-1] 中的墙都能摧毁
        return f1
