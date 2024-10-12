import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumLengthEncoding(test_input)

    def minimumLengthEncoding(self, words: List[str]) -> int:
        N = len(words)
        # 逆序字典序排序
        words.sort(key=lambda word: word[::-1])

        res = 0
        for i in range(N):
            if i + 1 < N and words[i + 1].endswith(words[i]):
                # 当前单词是下一个单词的后缀，丢弃
                pass
            else:
                res += len(words[i]) + 1  # 单词加上一个 '#' 的长度

        return res
