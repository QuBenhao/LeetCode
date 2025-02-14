import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxDistance(*test_input)

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def check(d):
            cnt = 1
            pre = position[0]
            for i in range(1, n):
                if position[i] - pre >= d:
                    cnt += 1
                    pre = position[i]
            return cnt >= m

        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = (l + r + 1) // 2
            if check(mid):
                l = mid
            else:
                r = mid - 1
        return l
