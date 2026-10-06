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

        # 1. Handle all 'T' constraints
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j
                    char = str2[j]
                    if fixed[pos]:
                        if word[pos] != char:
                            return ""  # Conflict; no solution
                    else:
                        word[pos] = char
                        fixed[pos] = True

        # 2. Fill undetermined positions with 'a' (lexicographically smallest)
        for i in range(total_len):
            if not fixed[i]:
                word[i] = 'a'

        # 3. Check and fix all 'F' constraints
        for i in range(n):
            if str1[i] == 'F':
                substring = ''.join(word[i:i+m])
                if substring == str2:
                    # Find an unfixed position to modify
                    modified = False
                    for j in range(m - 1, -1, -1):  # Search from right to left to keep the result lexicographically smallest
                        pos = i + j
                        if not fixed[pos]:
                            for c in range(ord(word[pos]) + 1, ord('z') + 1):
                                word[pos] = chr(c)
                                modified = True
                                break
                            if modified:
                                break
                    if not modified:
                        return ""  # No position can be changed; no solution

        return ''.join(word)

