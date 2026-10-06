import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.findTheString(test_input)

    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [''] * n

        # Step 1: construct the string greedily
        for i in range(n):
            # Find a position j with lcp > 0 relative to i; word[i] must equal word[j]
            for j in range(i):
                if lcp[i][j] > 0:
                    word[i] = word[j]
                    break

            # If none exists, assign a new character
            if word[i] == '':
                # Find the smallest usable character
                # It must differ from the character at every j with lcp[i][j] = 0
                used = set()
                for j in range(i):
                    if lcp[i][j] == 0:
                        used.add(word[j])

                # Choose the smallest available character
                for c in range(26):
                    ch = chr(ord('a') + c)
                    if ch not in used:
                        word[i] = ch
                        break

                # If all 26 letters are used, there is no solution
                if word[i] == '':
                    return ""

        # Step 2: validate the LCP matrix
        # Compute the LCP matrix for word
        computed = [[0] * n for _ in range(n)]

        # Fill from bottom right to top left using the recurrence
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word[i] == word[j]:
                    if i == n - 1 or j == n - 1:
                        computed[i][j] = 1
                    else:
                        computed[i][j] = computed[i + 1][j + 1] + 1
                else:
                    computed[i][j] = 0

        # Check whether it matches the given matrix
        for i in range(n):
            for j in range(n):
                if computed[i][j] != lcp[i][j]:
                    return ""

        return ''.join(word)

