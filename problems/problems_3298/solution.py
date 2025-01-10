from collections import defaultdict

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.validSubstringCount(*test_input)

    def validSubstringCount(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0

        # t 的字母出现次数与 s 的字母出现次数之差
        diff = defaultdict(int)  # 也可以用 Counter(t)，但是会慢很多
        for c in t:
            diff[c] += 1

        # 窗口内有 less 个字母的出现次数比 t 的少
        less = len(diff)

        ans = left = 0
        for c in s:
            diff[c] -= 1
            if diff[c] == 0:
                # c 移入窗口后，窗口内 c 的出现次数和 t 的一样
                less -= 1
            while less == 0:  # 窗口符合要求
                if diff[s[left]] == 0:
                    # s[left] 移出窗口之前，检查出现次数，
                    # 如果窗口内 s[left] 的出现次数和 t 的一样，
                    # 那么 s[left] 移出窗口后，窗口内 s[left] 的出现次数比 t 的少
                    less += 1
                diff[s[left]] += 1
                left += 1
            ans += left
        return ans
