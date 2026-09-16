from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minSumOfLengths(*test_input)

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # pre[i] = arr[:i] 中和为 target 的最短子数组长度（完全落在 i 左侧）
        pre = [inf] * (len(arr) + 1)
        last = {0: 0}  # 前缀和 -> 最晚出现位置，最晚即最短
        s = 0
        ans = inf
        for i, v in enumerate(arr, 1):
            s += v
            pre[i] = pre[i - 1]
            if s - target in last:
                j = last[s - target]  # 右侧子数组 arr[j:i]
                ans = min(ans, pre[j] + i - j)  # pre[j] 天然在 j 左侧 -> 不重叠
                pre[i] = min(pre[i], i - j)
            last[s] = i
        return ans if ans != inf else -1
