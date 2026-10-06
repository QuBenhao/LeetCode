import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.minimumLengthEncoding(test_input)

    def minimumLengthEncoding(self, words: List[str]) -> int:
        N = len(words)
        # Sort lexicographically by reversed words
        words.sort(key=lambda word: word[::-1])

        res = 0
        for i in range(N):
            if i + 1 < N and words[i + 1].endswith(words[i]):
                # The current word is a suffix of the next word; discard it
                pass
            else:
                res += len(words[i]) + 1  # Length of the word plus one '#'

        return res
