from itertools import zip_longest

import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.getWordsInLongestSubsequence(*test_input)

    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        def check(word1: str, word2: str) -> bool:
            return len(word1) == len(word2) and sum(c1 != c2 for c1, c2 in zip_longest(word1, word2)) == 1

        n = len(words)

        dp = [0] * n
        path = [-1] * n
        cur_max = n - 1

        for i in range(n-1, -1, -1):
            for j in range(i + 1, n):
                if dp[i] >= dp[j] or groups[i] == groups[j] or not check(words[i], words[j]):
                    continue
                dp[i] = dp[j]
                path[i] = j
            dp[i] += 1
            if dp[i] > dp[cur_max]:
                cur_max = i
        ans = [""] * dp[cur_max]
        k = cur_max
        for i in range(dp[cur_max]):
            ans[i] = words[k]
            k = path[k]
        return ans

