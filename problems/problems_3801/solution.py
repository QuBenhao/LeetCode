from bisect import bisect_right
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minMergeCost(test_input)

    def minMergeCost(self, lists: List[List[int]]) -> int:
        n = len(lists)
        total = 1 << n
        g, h = [0] * total, [0] * total
        for i in range(1, total):
            for j in range(n):
                if (i >> j) & 1:
                    g[i] += len(lists[j])
            head, tail = -int(1e9), int(1e9)
            while head < tail:
                mid = (head + tail) >> 1
                cnt = 0
                for j in range(n):
                    if (i >> j) & 1:
                        cnt += bisect_right(lists[j], mid)
                if cnt >= (g[i] + 1) // 2:
                    tail = mid
                else:
                    head = mid + 1
            h[i] = head

        f = [inf] * total
        for j in range(n):
            f[1 << j] = 0
        for i in range(1, total):
            if f[i] == 0:
                continue
            j = (i - 1) & i
            while j: # 枚举子集
                k = i ^ j
                f[i] = min(f[i], f[j] + f[k] + g[j] + g[k] + abs(h[j] - h[k]))
                j = (j - 1) & i
        return f[total - 1]
