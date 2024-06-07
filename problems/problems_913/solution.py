import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.catMouseGame(test_input)

    def catMouseGame(self, graph: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(m, c, i):
            """
            极大极小博弈，
            老鼠尽量找自己获胜的，其次接受平局
            猫尽量找自己获胜的，其次接受平局

            :param m: 老鼠的位置
            :param c: 猫的位置
            :param i: 回合
            """
            if i > 2 * (len(graph) ** 2):
                return 0
            if not m:
                return -1
            if c == m:
                return 1
            res = (-1) ** i
            if i % 2:
                for nxt in graph[c]:
                    if nxt:
                        res = max(res, dfs(m, nxt, i + 1))
                    if res == 1:
                        break
            else:
                for nxt in graph[m]:
                    res = min(res, dfs(nxt, c, i + 1))
                    if res == -1:
                        break
            return res
        return ans if not (ans:=dfs(1, 2, 0)) else (1 if ans == -1 else 2)

