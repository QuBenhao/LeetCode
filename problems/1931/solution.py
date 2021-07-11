import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.colorTheGrid(test_input[0], test_input[1])

    def colorTheGrid(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        @lru_cache(None)
        def dfs(i, j, colors):
            if i == m - 1 and j == n - 1:
                if colors[0] == -1 and colors[-1] == -1:
                    return 3
                elif colors[0] == -1 or colors[-1] == -1:
                    return 2
                return 2 if colors[0] == colors[-1] else 1
            tmp = list(colors[1:])
            ans = 0
            # 列的最底部要进入下一列
            if i == m - 1:
                for k in range(3):
                    if k != colors[0] and k != colors[-1]:
                        ans += dfs(0, j + 1, tuple(tmp + [k]))
            else:
                for k in range(3):
                    # 列的最顶部时上边的格子颜色不影响当前的选择
                    if (i and k != colors[0] and k != colors[-1]) or (not i and k != colors[0]):
                        ans += dfs(i + 1, j, tuple(tmp + [k]))
            return ans % (10 ** 9 + 7)

        return dfs(0, 0, tuple([-1] * m))