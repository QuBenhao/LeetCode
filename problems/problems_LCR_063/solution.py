import solution
from typing import *


class Solution(solution.Solution):
    def solve(self, test_input=None):
        return self.replaceWords(*test_input)

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        for word in dictionary:
            node = trie
            for c in word:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node['#'] = word

        def search(word):
            node = trie
            for c in word:
                if c not in node:
                    break
                node = node[c]
                if '#' in node:
                    return node['#']
            return word

        return " ".join(search(word) for word in sentence.split())
