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
        # 预处理，连续的由相同字符组成的子串看做一个,比如"aaabbb"和"ab"是没有区别的
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
            # j和i是相同的，那么打印i到j和打印i到j-1所需的次数是一样的(或者说i+1到j)
            if building[i] == building[j]:
                return dfs(i, j - 1)
            # i和j是不同的,找到一个最优的拆分方式
            return min(dfs(i, k) + dfs(k + 1, j) for k in range(i, j)
                       if building[k] == building[i] or building[k] == building[j])

        return dfs(0, len(building) - 1)
