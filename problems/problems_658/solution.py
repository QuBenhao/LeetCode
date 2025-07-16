from bisect import bisect_right
from collections import deque

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findClosestElements(*test_input)

    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_right(arr, x)
        left = idx - 1
        x *= 2
        while k and left >= 0 and idx < len(arr):
            if arr[left] + arr[idx] >= x:
                left -= 1
            else:
                idx += 1
            k -= 1
        if k:
            if idx == len(arr):
                left -= k
            else:
                idx += k
        return arr[left+1:idx]
