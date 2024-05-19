import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.wordBreak(*test_input)

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n, words, ml = len(s), set(wordDict), max(len(word) for word in wordDict)
        cur = {0}
        for i in range(1, n + 1):
            tmp = set(cur)
            for idx in tmp:
                if i - idx > ml:
                    cur.remove(idx)
                    continue
                if idx < i and s[idx:i] in words:
                    cur.add(i)
                    break
        return n in cur
