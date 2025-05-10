from math import inf

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.largestVariance(test_input)

    def largestVariance(self, s: str) -> int:
        # 按小写字母枚举
        f0 = [[0] * 26 for _ in range(26)] # 表示最大子数组和中, -1不一定出现
        f1 = [[-inf] * 26 for _ in range(26)] # 表示最大子数组和中, -1一定出现
        ans = 0
        for ch in map(ord, s):
            ch -= ord("a")
            for i in range(26):
                if i == ch:
                    continue
                f0[ch][i] = max(0, f0[ch][i]) + 1
                f1[ch][i] += 1
                f1[i][ch] = f0[i][ch] = max(f0[i][ch], 0) - 1
                # 循环内更新最大方便统计了所有子串
                ans = max(ans, f1[ch][i], f1[i][ch])
        return ans
