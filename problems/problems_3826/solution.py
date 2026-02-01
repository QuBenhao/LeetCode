from itertools import accumulate
from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minPartitionScore(*test_input)

    def minPartitionScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = list(accumulate(nums, initial=0))
        f = [0] + [inf] * n

        for K in range(1, k + 1):
            s = pre[K - 1]
            q = [Vec(s, f[K - 1] + s * s - s)]
            for i in range(K, n - (k - K) + 1):
                s = pre[i]
                p = Vec(-2 * s, 1)
                while len(q) > 1 and p.dot(q[0]) >= p.dot(q[1]):
                    q = q[1:]

                v = Vec(s, f[i] + s * s - s)
                f[i] = p.dot(q[0]) + s * s + s

                while len(q) > 1 and (q[-1] - q[-2]).det(v - q[-1]) <= 0:
                    q.pop()
                q.append(v)

        return f[n] // 2


class Vec:
    __slots__ = 'x', 'y'

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __sub__(self, b: Vec) -> Vec:
        return Vec(self.x - b.x, self.y - b.y)

    def det(self, b: Vec) -> int:
        return self.x * b.y - self.y * b.x

    def dot(self, b: Vec) -> int:
        return self.x * b.x + self.y * b.y
