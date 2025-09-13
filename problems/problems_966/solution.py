import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.spellchecker(*test_input)

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        origin = set()
        ignore_cases = dict()
        ignore_vowels = dict()

        def str_to_ignore_vowels(w: str) -> str:
            w = w.lower()
            res = []
            for c in w:
                if c in VOWELS:
                    res.append('*')
                else:
                    res.append(c)
            return "".join(res)

        for word in wordlist:
            origin.add(word)
            if (l := word.lower()) not in ignore_cases:
                ignore_cases[l] = word
            if (l := str_to_ignore_vowels(word)) not in ignore_vowels:
                ignore_vowels[l] = word
        ans = []
        for query in queries:
            if query in origin:
                ans.append(query)
                continue
            if (l := query.lower()) in ignore_cases:
                ans.append(ignore_cases[l])
                continue
            if (l := str_to_ignore_vowels(query)) in ignore_vowels:
                ans.append(ignore_vowels[l])
                continue
            ans.append("")
        return ans

VOWELS = "aeiouAEIOU"
