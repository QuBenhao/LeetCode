import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findTheString(test_input)

    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [''] * n

        # 步骤1：构造字符串（贪心）
        for i in range(n):
            # 找到与位置 i 有 lcp > 0 的位置 j，则 word[i] 必须等于 word[j]
            for j in range(i):
                if lcp[i][j] > 0:
                    word[i] = word[j]
                    break

            # 如果没有找到，则需要分配一个新的字符
            if word[i] == '':
                # 找到能用的最小字符
                # 必须与所有 lcp[i][j] = 0 的位置 j 的字符不同
                used = set()
                for j in range(i):
                    if lcp[i][j] == 0:
                        used.add(word[j])

                # 选择最小可用字符
                for c in range(26):
                    ch = chr(ord('a') + c)
                    if ch not in used:
                        word[i] = ch
                        break

                # 如果26个字母都用完了，无解
                if word[i] == '':
                    return ""

        # 步骤2：验证 LCP 矩阵
        # 计算 word 对应的 LCP 矩阵
        computed = [[0] * n for _ in range(n)]

        # 从右下角向左上角填充（利用递推关系）
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    if i == n - 1 or j == n - 1:
                        computed[i][j] = 1
                    else:
                        computed[i][j] = computed[i + 1][j + 1] + 1
                else:
                    computed[i][j] = 0

        # 验证是否与给定矩阵一致
        for i in range(n):
            for j in range(n):
                if computed[i][j] != lcp[i][j]:
                    return ""

        return ''.join(word)

