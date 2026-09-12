import solution
from typing import *
from bisect import bisect_left


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maximumWeight(test_input)

    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # 按右端点升序，选中的区间在排序后构成一条链（后一个的左端点 > 前一个的右端点）
        order = sorted(range(n), key=lambda i: intervals[i][1])
        rs = [intervals[i][1] for i in order]
        # pref[k][p]：前 p+1 个区间里选 k 个互不重叠的最优 (得分, 升序下标元组)
        pref = [[None] * n for _ in range(4)]
        ans = (0, ())
        for p, i in enumerate(order):
            l, r, w = intervals[i]
            cur = [None] * 4
            cur[0] = (w, (i,))
            lim = bisect_left(rs, l) - 1  # 最后一个满足 r < l 的位置，即能接在 i 前面的区间
            if lim >= 0:
                for k in range(1, 4):
                    bp = pref[k - 1][lim]
                    if bp:
                        cur[k] = (bp[0] + w, tuple(sorted(bp[1] + (i,))))
            for k in range(4):
                prev = pref[k][p - 1] if p else None
                best = cur[k]
                if prev and (not best or prev[0] > best[0] or (prev[0] == best[0] and prev[1] < best[1])):
                    best = prev
                pref[k][p] = best
                if best and (best[0] > ans[0] or (best[0] == ans[0] and best[1] < ans[1])):
                    ans = best
        return list(ans[1])
