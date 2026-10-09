import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minInsertions(test_input)

    def minInsertions(self, s: str) -> int:
        # need: 当前还缺多少个 ')'（欠账）
        ans = need = 0
        for c in s:
            if c == '(':
                if need % 2:  # 前面有落单的 ')'，补一个凑成 '))'
                    ans += 1
                    need -= 1
                need += 2
            elif need:
                need -= 1
            else:  # 无人认领的 ')'，补一个 '('，还缺一个 ')'
                ans += 1
                need = 1
        return ans + need
