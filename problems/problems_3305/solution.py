import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.countOfSubstrings(*test_input)

    def countOfSubstrings(self, word: str, k: int) -> int:
        # 恰好k个 = 至少k个 - 至少k+1个
        vowels = {'a', 'e', 'i', 'o', 'u'}

        def count(m: int) -> int:
            n, res, consonants = len(word), 0, 0
            occur = {}
            j = 0
            for i in range(n):
                while j < n and (consonants < m or len(occur) < 5):
                    if word[j] in vowels:
                        occur[word[j]] = occur.get(word[j], 0) + 1
                    else:
                        consonants += 1
                    j += 1
                if consonants >= m and len(occur) == 5:
                    res += n - j + 1
                if word[i] in vowels:
                    occur[word[i]] -= 1
                    if occur[word[i]] == 0:
                        del occur[word[i]]
                else:
                    consonants -= 1
            return res

        return count(k) - count(k + 1)
