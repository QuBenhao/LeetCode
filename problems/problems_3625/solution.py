from collections import defaultdict
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countTrapezoids(test_input)

    def countTrapezoids(self, points: List[List[int]]) -> int:
        cnt = defaultdict(lambda: defaultdict(int))  # 斜率 -> 截距 -> 个数
        cnt2 = defaultdict(lambda: defaultdict(int))  # 中点 -> 斜率 -> 个数

        for i, (x, y) in enumerate(points):
            for x2, y2 in points[:i]:
                dy = y - y2
                dx = x - x2
                if dx == 0:
                    k = inf
                    b = float(x)
                else:
                    k = dy / dx
                    b = (y * dx - dy * x) / dx
                cnt[k][b] += 1  # 按照斜率和截距分组
                cnt2[(x + x2, y + y2)][k] += 1  # 按照中点和斜率分组

        ans = 0
        for ct in cnt.values():
            s = 0
            for c in ct.values():
                ans += s * c
                s += c

        for ct in cnt2.values():
            s = 0
            for c in ct.values():
                ans -= s * c
                s += c

        return ans
