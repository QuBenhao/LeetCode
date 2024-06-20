import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.validWordSquare(test_input)

    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            if len(words[i]) > len(words):
                return False
            for j in range(i):
                if ((len(words[i]) <= j) != (len(words[j]) <= i)):
                    return False
                elif len(words[i]) > j and words[i][j] != words[j][i]:
                    return False
        return True
