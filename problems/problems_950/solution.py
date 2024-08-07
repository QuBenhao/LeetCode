import solution
from typing import *
from collections import deque


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.deckRevealedIncreasing(test_input)

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q = deque()
        while deck:
            if q:
                q.appendleft(q.pop())
            q.appendleft(deck.pop())
        return list(q)
