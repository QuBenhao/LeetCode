import solution
from functools import lru_cache


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxCompatibilitySum(*test_input)

    def maxCompatibilitySum(self, students, mentors):
        """
        :type students: List[List[int]]
        :type mentors: List[List[int]]
        :rtype: int
        """
        m, n = len(students), len(students[0])

        def cal(a, b):
            return sum(a[i] == b[i] for i in range(n))

        @lru_cache(None)
        def dfs(i, mts):
            if i == m:
                return 0
            curr = list(mts)
            return max(dfs(i + 1, tuple(curr[:j] + curr[j + 1:])) + cal(students[i], mentors[curr[j]]) for j in range(len(curr)))

        return dfs(0, tuple([i for i in range(m)]))
