import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.answerString(*test_input)

    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        return max(word[i:i+n-numFriends+1] for i in range(n))
