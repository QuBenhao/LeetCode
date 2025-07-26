import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxSubarrays(*test_input)

    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        g0 = [n + 1] * (n + 1)
        g1 = [n + 1] * (n + 1)
        for a, b in conflictingPairs:
            if a > b:
                a, b = b, a
            # 维护a前二小的右端点b，这样删除一个冲突对时，右端点可以快速取到
            if b < g0[a]:
                g1[a] = g0[a]
                g0[a] = b
            elif b < g1[a]:
                g1[a] = b

        ans = max_extra = extra = 0
        b0 = b1 = n + 1
        for i in range(n, 0, -1):
            pre_b0 = b0

            b, c = g0[i], g1[i]
            if b < b0:
                b1 = min(b0, c)
                b0 = b
            elif b < b1:
                b1 = b
            elif c < b1:
                b1 = c

            ans += b0 - i
            if b0 != pre_b0:  # 重新统计连续相同 b0 的 extra
                extra = 0
            extra += b1 - b0
            max_extra = max(max_extra, extra)

        return ans + max_extra
