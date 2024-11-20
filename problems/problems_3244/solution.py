import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.shortestDistanceAfterQueries(*test_input)

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        fa = list(range(n - 1))

        # 非递归并查集
        def find(x: int) -> int:
            rt = x
            while fa[rt] != rt:
                rt = fa[rt]
            while fa[x] != rt:
                fa[x], x = rt, fa[x]
            return rt

        ans = []
        cnt = n - 1  # 并查集连通块个数
        for l, r in queries:
            fr = find(r - 1)
            i = find(l)
            while i < r - 1:
                cnt -= 1
                fa[i] = fr
                i = find(i + 1)
            ans.append(cnt)
        return ans
