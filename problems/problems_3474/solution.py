import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.generateString(*test_input)

    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        total_len = n + m - 1

        word = [''] * total_len
        fixed = [False] * total_len

        # 1. 处理所有 'T' 约束
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j
                    char = str2[j]
                    if fixed[pos]:
                        if word[pos] != char:
                            return ""  # 冲突，无解
                    else:
                        word[pos] = char
                        fixed[pos] = True

        # 2. 填充未确定的位置为 'a'（字典序最小）
        for i in range(total_len):
            if not fixed[i]:
                word[i] = 'a'

        # 3. 检查并修正所有 'F' 约束
        for i in range(n):
            if str1[i] == 'F':
                substring = ''.join(word[i:i+m])
                if substring == str2:
                    # 需要找一个未固定的位置修改
                    modified = False
                    for j in range(m - 1, -1, -1):  # 从后往前找，保证字典序最小
                        pos = i + j
                        if not fixed[pos]:
                            for c in range(ord(word[pos]) + 1, ord('z') + 1):
                                word[pos] = chr(c)
                                modified = True
                                break
                            if modified:
                                break
                    if not modified:
                        return ""  # 无法修改，无解

        return ''.join(word)

