from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxTurbulenceSize(test_input)

    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 1
        last = [1, 1] # 第一位表示下降，第二位表示上升
        for i in range(1, n):
            cur_0 = cur_1 = 1
            if arr[i] > arr[i-1]:
                cur_1 += last[0]
            elif arr[i] < arr[i-1]:
                cur_0 += last[1]
            ans = max(ans, cur_0, cur_1)
            last[0], last[1] = cur_0, cur_1
        return ans
