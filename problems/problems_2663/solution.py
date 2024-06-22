import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallestBeautifulString(*test_input)

    def smallestBeautifulString(self, s: str, k: int) -> str:
        a = ord('a')
        k += a
        s = list(map(ord, s))
        n = len(s)
        i = n - 1  # 从最后一个字母开始
        s[i] += 1  # 先加一
        while i < n:
            if s[i] == k:  # 需要进位
                if i == 0:  # 无法进位
                    return ""
                # 进位
                s[i] = a
                i -= 1
                s[i] += 1
            elif i and s[i] == s[i - 1] or i > 1 and s[i] == s[i - 2]:
                s[i] += 1  # 如果 s[i] 和左侧的字符形成回文串，就继续增加 s[i]
            else:
                i += 1  # 反过来检查后面是否有回文串
        return ''.join(map(chr, s))
