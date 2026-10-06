import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.smallestSubsequence(*test_input)

    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        letter_left = s.count(letter)
        ans = []
        cur_letter = 0
        n = len(s)
        for i, c in enumerate(s):
            # Condition 1: an increasing monotonic stack ensures the smallest lexicographic order
            # Condition 2: ensure length k (n-i characters remain, len(ans) are already selected, and removing the stack top must still allow length k)
            # Condition 3: ensure at least repetition occurrences of letter
            while (ans and ans[-1] > c and n - i + len(ans) - 1 >= k and
                   (c == letter or letter_left + cur_letter - (ans[-1] == letter) >= repetition)):
                if ans.pop() == letter:
                    cur_letter -= 1
            if len(ans) < k:
                if c == letter:
                    cur_letter += 1
                    ans.append(c)
                elif k - len(ans) > repetition - cur_letter:
                    ans.append(c)
            if c == letter:
                letter_left -= 1
        return "".join(ans)
