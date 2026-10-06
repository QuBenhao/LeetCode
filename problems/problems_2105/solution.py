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
            # Alice waters plant i
            if a < plants[i]:
                # Not enough water; refill the watering can
                ans += 1
                a = capacityA
            a -= plants[i]
            i += 1
            # Bob waters plant j
            if b < plants[j]:
                # Not enough water; refill the watering can
                ans += 1
                b = capacityB
            b -= plants[j]
            j -= 1
        # If Alice and Bob reach the same plant, the person with more water remaining waters it
        if i == j and max(a, b) < plants[i]:
            # Not enough water; refill the watering can
            ans += 1
        return ans
