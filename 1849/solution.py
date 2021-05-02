import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.splitString(str(test_input))

    def splitString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        @lru_cache(None)
        def dfs(st, curr):
            if not st:
                return True
            if curr is not None:
                for idx in range(1, len(st) + 1):
                    if int(st[:idx]) == curr - 1 and dfs(st[idx:], curr - 1):
                        return True
                    elif int(st[:idx]) > curr - 1:
                        break
            else:
                for idx in range(1, len(st)):
                    if dfs(st[idx:], int(st[:idx])):
                        return True
            return False

        return dfs(s, None)
