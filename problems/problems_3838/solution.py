import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.mapWordWeights(*test_input)

    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ""
        for word in words:
            cur = 0
            for c in word:
                cur = (cur + weights[ord(c) - ord('a')]) % 26
            ans += chr(ord('z') - cur)
        return ans
