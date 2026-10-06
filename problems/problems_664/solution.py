import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.strangePrinter(str(test_input))

    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Preprocess runs of identical characters as one character; for example, "aaabbb" and "ab" are equivalent
        building = [s[0]]
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                building.append(s[i])

        @lru_cache(None)
        def dfs(i, j):
            if i > j:
                return 0
            elif i == j:
                return 1
            # If the characters at j and i match, printing i through j takes as many turns as i through j-1 (or i+1 through j)
            if building[i] == building[j]:
                return dfs(i, j - 1)
            # The characters at i and j differ; find the optimal split
            return min(dfs(i, k) + dfs(k + 1, j) for k in range(i, j)
                       if building[k] == building[i] or building[k] == building[j])

        return dfs(0, len(building) - 1)
