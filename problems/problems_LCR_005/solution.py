from collections import defaultdict
from itertools import combinations

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.maxProduct(test_input)

    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        word_dict = defaultdict(int)
        for i, word in enumerate(words):
            cur = 0
            for c in word:
                cur |= 1 << (ord(c) - ord('a'))
            word_dict[cur] = max(word_dict[cur], len(word))
        for k1, k2 in combinations(word_dict.keys(), 2):
            if k1 & k2 == 0:
                ans = max(ans, word_dict[k1] * word_dict[k2])
        return ans
