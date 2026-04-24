import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxDistance(*test_input)

    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        a = []
        for x, y in points:
            if x == 0:
                a.append(y)
            elif y == side:
                a.append(side + x)
            elif x == side:
                a.append(side * 3 - y)
            else:
                a.append(side * 4 - x)
        a.sort()

        n = len(a)
        f = [0] * (n + 1)
        end = [0] * n

        def check(low: int) -> bool:
            j = n
            for i in range(n - 1, -1, -1):
                while a[j - 1] >= a[i] + low:
                    j -= 1
                f[i] = f[j] + 1
                end[i] = end[j] if f[i] > 1 else i
                if f[i] == k and a[end[i]] - a[i] <= side * 4 - low:
                    return True
            return False

        left, right = 1, side * 4 // k + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
        return left
