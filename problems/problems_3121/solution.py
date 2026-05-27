import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.numberOfSpecialChars(test_input)

    def numberOfSpecialChars(self, word: str) -> int:
        """
        Count special characters where:
        1. Character appears in both lowercase and uppercase
        2. ALL lowercase occurrences appear BEFORE the first uppercase occurrence
        """
        # Track: first uppercase position, last lowercase position for each letter
        first_upper = [-1] * 26  # First uppercase position for each letter
        last_lower = [-1] * 26   # Last lowercase position for each letter

        for i, c in enumerate(word):
            idx = ord(c.lower()) - ord('a')
            if c.isupper():
                if first_upper[idx] == -1:
                    first_upper[idx] = i
            else:
                last_lower[idx] = i

        # Count special characters
        # A letter is special if:
        # - It appears in both cases (first_upper[idx] != -1 and last_lower[idx] != -1)
        # - All lowercase before first uppercase (last_lower[idx] < first_upper[idx])
        count = 0
        for idx in range(26):
            if first_upper[idx] != -1 and last_lower[idx] != -1:
                if last_lower[idx] < first_upper[idx]:
                    count += 1

        return count