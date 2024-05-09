import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumRefill(*test_input)

    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        ans = 0
        a, b = capacityA, capacityB
        i, j = 0, len(plants) - 1
        while i < j:
            # Alice 给植物 i 浇水
            if a < plants[i]:
                # 没有足够的水，重新灌满水罐
                ans += 1
                a = capacityA
            a -= plants[i]
            i += 1
            # Bob 给植物 j 浇水
            if b < plants[j]:
                # 没有足够的水，重新灌满水罐
                ans += 1
                b = capacityB
            b -= plants[j]
            j -= 1
        # Alice 和 Bob 到达同一株植物，那么当前水罐中水更多的人会给这株植物浇水
        if i == j and max(a, b) < plants[i]:
            # 没有足够的水，重新灌满水罐
            ans += 1
        return ans
