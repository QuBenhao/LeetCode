from typing import List

import solution


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findDiagonalOrder(test_input)

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n, ans = len(mat), len(mat[0]), []
        for k in range(m + n - 1):
            if not k % 2:
                ans += [mat[x][k-x] for x in range(min(m - 1, k), max(-1, k - n),-1)]
            else:
                ans += [mat[x][k-x] for x in range(max(0, k - n + 1), min(k + 1, m))]
        return ans
