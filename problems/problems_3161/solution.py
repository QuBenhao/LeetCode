from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getResults(test_input)

    def getResults(self, queries: List[List[int]]) -> List[bool]:
        m = max(q[1] for q in queries) + 1
        t = [0] * m

        def update(i: int, val: int) -> None:
            while i < m:
                t[i] = max(t[i], val)
                i += i & -i

        def pre_max(i: int) -> int:
            res = 0
            while i:
                res = max(res, t[i])
                i &= i - 1
            return res

        left = list(range(m + 1))
        right = left.copy()

        def find(fa: List[int], x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa, fa[x])
            return fa[x]

        pos = [0] + sorted(q[1] for q in queries if q[0] == 1)
        for p, q in pairwise(pos):
            update(q, q - p)
            for j in range(p + 1, q):
                left[j] = p  # 删除 j
                right[j] = q
        for j in range(pos[-1] + 1, m):
            left[j] = pos[-1]  # 删除 j
            right[j] = m

        ans = []
        for q in reversed(queries):
            x = q[1]
            pre = find(left, x - 1)  # x 左侧最近障碍物的位置
            if q[0] == 1:
                left[x] = x - 1  # 删除 x
                right[x] = x + 1
                nxt = find(right, x)  # x 右侧最近障碍物的位置
                update(nxt, nxt - pre)  # 更新 d[nxt] = nxt - pre
            else:
                # 最大长度要么是 [0,pre] 中的最大 d，要么是 [pre,x] 这一段的长度
                max_gap = max(pre_max(pre), x - pre)
                ans.append(max_gap >= q[2])

        ans.reverse()
        return ans
