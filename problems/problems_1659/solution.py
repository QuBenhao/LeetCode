import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getMaxGridHappiness(*test_input)

    def getMaxGridHappiness(self, m, n, introvertsCount, extrovertsCount):
        """
        :type m: int
        :type n: int
        :type introvertsCount: int
        :type extrovertsCount: int
        :rtype: int
        """

        @lru_cache(None)
        def dfs(x, y, intro, extro, state):
            if y == n:
                return dfs(x + 1, 0, intro, extro, state)
            if x == m:
                return 0
            # 最近的n个安排，再多不会被当前的影响到
            l = list(state)
            # 上面的人是l[0]，左边的人是l[-1]

            # 什么也不填
            ans = dfs(x, y + 1, intro, extro, tuple(l[1:] + [0]))

            # 填入一个内向
            if intro:
                diff = 120
                if l[0] == 1:
                    diff -= 30 * 2
                elif l[0] == 2:
                    # 一个内向一个外向
                    diff -= 10
                if y:
                    if l[-1] == 1:
                        diff -= 30 * 2
                    elif l[-1] == 2:
                        diff -= 10
                ans = max(ans, dfs(x, y + 1, intro - 1, extro, tuple(l[1:] + [1])) + diff)

            # 填入一个外向
            if extro:
                diff = 40
                if l[0] == 1:
                    diff -= 10
                elif l[0] == 2:
                    diff += 40
                if y:
                    if l[-1] == 1:
                        diff -= 10
                    elif l[-1] == 2:
                        diff += 40
                ans = max(ans, dfs(x, y + 1, intro, extro - 1, tuple(l[1:] + [2])) + diff)
            return ans

        return dfs(0, 0, introvertsCount, extrovertsCount, tuple([0] * n))
