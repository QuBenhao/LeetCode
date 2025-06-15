import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.removeDuplicateLetters(test_input)

    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        explored = set()
        last_idx = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in explored:
                while stack and c < stack[-1] and i < last_idx[stack[-1]]:
                    explored.remove(stack.pop())
                stack.append(c)
                explored.add(c)
        return ''.join(stack)
