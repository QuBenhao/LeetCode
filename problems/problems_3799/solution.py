from itertools import permutations

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.wordSquares(test_input)

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        words.sort()
        return [[top, left, right, bottom] for top, left, right, bottom in permutations(words, 4)
                if top[0] == left[0] and top[3] == right[0] and bottom[0] == left[3] and bottom[3] == right[3]]
