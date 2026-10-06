from bisect import bisect_left

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxTotalFruits(*test_input)

    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left = bisect_left(fruits, startPos - k, key=lambda x: x[0])
        right = bisect_left(fruits, startPos + 1, key=lambda x: x[0])
        ans = s = sum(fruit[1] for fruit in fruits[left:right])
        n = len(fruits)
        while right < n and fruits[right][0] <= startPos + k:
            s += fruits[right][1]
            # Left first, then right: (startPos - fruits[left][0]) + (fruits[right][0] - fruits[left][0])
            # Right first, then left: (fruits[right][0] - startPos) + (fruits[right][0] - fruits[left][0])
            # If neither route can cover the window, move left to the right
            while fruits[right][0] * 2 - fruits[left][0] - startPos > k and startPos + fruits[right][0] - fruits[left][0] * 2 > k:
                s -= fruits[left][1]
                left += 1
            ans = max(ans, s)
            right += 1
        return ans
