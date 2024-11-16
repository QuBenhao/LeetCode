import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minFlips(test_input)

    def minFlips(self, a: List[List[int]]) -> int:
        m, n = len(a), len(a[0])
        ans = 0
        for i in range(m // 2):
            row, row2 = a[i], a[-1 - i]
            for j in range(n // 2):
                cnt1 = row[j] + row[-1 - j] + row2[j] + row2[-1 - j]
                ans += min(cnt1, 4 - cnt1)  # 全为 1 或全为 0

        if m % 2 and n % 2:
            # 正中间的数必须是 0
            ans += a[m // 2][n // 2]

        diff = cnt1 = 0
        if m % 2:
            # 统计正中间这一排
            row = a[m // 2]
            for j in range(n // 2):
                if row[j] != row[-1 - j]:
                    diff += 1
                else:
                    cnt1 += row[j] * 2
        if n % 2:
            # 统计正中间这一列
            for i in range(m // 2):
                if a[i][n // 2] != a[-1 - i][n // 2]:
                    diff += 1
                else:
                    cnt1 += a[i][n // 2] * 2

        return ans + (diff if diff else cnt1 % 4)        
