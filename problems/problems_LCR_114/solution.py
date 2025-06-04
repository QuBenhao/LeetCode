from collections import defaultdict, deque
from itertools import pairwise

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.alienOrder(test_input)

    def alienOrder(self, words: List[str]) -> str:
        def build(word1, word2) -> bool:
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in graph[c1]:
                        # c1 -> c2
                        # c1 must come before c2
                        indegree[c2] += 1
                    graph[c1].add(c2)
                    return True

            return len(word1) <= len(word2)

        chars = set(words[0])
        graph = defaultdict(set)
        indegree = defaultdict(int)

        for a, b in pairwise(words):
            chars.update(b)
            if not build(a, b):
                return ""
        queue = deque([c for c in chars if indegree[c] == 0])
        result = []
        while queue:
            c = queue.popleft()
            result.append(c)
            for neighbor in graph[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        if len(result) < len(chars):
            return ""
        return ''.join(result)
