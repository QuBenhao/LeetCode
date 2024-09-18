import string

import solution
from typing import *
import heapq


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.ladderLength(*test_input)

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def distance(word1, word2):
            return sum([1 for i in range(len(word1)) if word1[i] != word2[i]])

        words = set(wordList)
        if endWord not in words:
            return 0
        pq = [(0, 0, beginWord)]
        costs = {beginWord: 0}
        while pq:
            _, cost, word = heapq.heappop(pq)
            if word == endWord:
                return cost + 1
            for i, c in enumerate(word):
                for new_c in string.ascii_lowercase:
                    if new_c == c:
                        continue
                    t = word[:i] + new_c + word[i+1:]
                    if t in words and (t not in costs or cost + 1 < costs[t]):
                        costs[t] = cost + 1
                        heapq.heappush(pq, (cost + 1 + distance(t, endWord), cost + 1, t))
        return 0
