import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.reorderSpaces(test_input)

    def reorderSpaces(self, text: str) -> str:
        words = []
        space = 0
        left = -1
        for i, c in enumerate(text + ' '):
            if c == ' ':
                space += 1
                if left != -1:
                    words.append(text[left:i])
                    left = -1
            elif left == -1:
                left = i
        print(words, space, f"\"{text}\"")
        space -= 1
        if len(words) == 1:
            return words[0] + ' ' * space
        d, r = divmod(space, len(words) - 1)
        return (' ' * d).join(words) + ' ' * r
