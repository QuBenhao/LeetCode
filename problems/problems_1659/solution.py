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
            # Keep the last n placements; earlier cells cannot be affected by this one
            l = list(state)
            # The upper neighbor is l[0], and the left neighbor is l[-1]

            # Leave the cell empty
            ans = dfs(x, y + 1, intro, extro, tuple(l[1:] + [0]))

            # Place an introvert
            if intro:
                diff = 120
                if l[0] == 1:
                    diff -= 30 * 2
                elif l[0] == 2:
                    # One introvert and one extrovert
                    diff -= 10
                if y:
                    if l[-1] == 1:
                        diff -= 30 * 2
                    elif l[-1] == 2:
                        diff -= 10
                ans = max(ans, dfs(x, y + 1, intro - 1, extro, tuple(l[1:] + [1])) + diff)

            # Place an extrovert
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
